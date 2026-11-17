# Name: Michael Breaux
# Course: CS361 - Software Engineering I
# Assignment: 7 - Small Pool Implementation
# Description: Sort & Filter microservice.
# Sorts records by date or climbing grade and filters by field.

from flask import Flask, request, jsonify
from datetime import date
import re

app = Flask(__name__)


def sort_records(records, field, order="ascending"):
    """Sort records by the requested field without changing the original list."""

    reverse = order == "descending"

    # Sort climbing grades by their numeric value (V2, V5, V10)
    if field == "grade":
        def grade_key(record):
            grade = str(record[field]).upper()
            match = re.fullmatch(r"V(\d+)", grade)

            if match:
                return int(match.group(1))

            return grade

        return sorted(records, key=grade_key, reverse=reverse)

    # Sort dates chronologically instead of alphabetically
    if field == "date":
        return sorted(
            records,
            key=lambda record: date.fromisoformat(record[field]),
            reverse=reverse
        )

    # Sort other fields alphabetically or numerically
    return sorted(
        records,
        key=lambda record: record[field],
        reverse=reverse
    )


def filter_records(records, field, value):
    """Return only records matching the requested field and value."""

    return [
        record for record in records
        if record.get(field) == value
    ]


@app.route("/process", methods=["POST"])
def process_records():
    """Receive a JSON request and return sorted or filtered records."""

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Request body must be JSON."}), 400

    operation = data.get("operation")
    records = data.get("records", [])
    field = data.get("field")
    order = data.get("order", "ascending")
    value = data.get("value")

    if not isinstance(records, list):
        return jsonify({"error": "records must be a list of objects."}), 400
    if not field:
        return jsonify({"error": "field is required, like \"date\"."}), 400

    try:
        if operation == "sort":
            for record in records:
                if field not in record:
                    return jsonify({"error": "Field '" + field + "' was not found in the records."}), 400
            result = sort_records(records, field, order)
        elif operation == "filter":
            result = filter_records(records, field, value)
        else:
            return jsonify({"error": "Invalid operation. Use \"sort\" or \"filter\"."}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid value in field '" + field + "'. Dates must look like 2026-11-08 and grades like V5."}), 400

    return jsonify({"records": result}), 200


if __name__ == "__main__":
    app.run(port=5001, debug=True)
