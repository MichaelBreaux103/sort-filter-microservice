# Name: Michael Breaux
# Course: CS361 - Software Engineering I
# Assignment: 7 - Small Pool Implementation
# Description: Test program for the Sort & Filter microservice.
# Sends requests and displays the responses from the microservice.

import requests
import json

# Address of the Sort & Filter microservice
SERVICE_URL = "http://127.0.0.1:5001/process"

# Sample climbing sessions used for testing
sessions = [
    {"date": "2026-11-08", "grade": "V5", "location": "Movement"},
    {"date": "2026-11-03", "grade": "V10", "location": "The Spot"},
    {"date": "2026-11-06", "grade": "V2", "location": "Movement"}
]


def send_request(description, payload):
    """Send a request to the microservice and display its response."""

    print(f"\n--- {description} ---")

    # Send the JSON request to the microservice
    try:
        response = requests.post(
            SERVICE_URL,
            json=payload,
            timeout=5
        )

        # Receive and display the JSON response
        print(f"HTTP Status: {response.status_code}")
        print(json.dumps(response.json(), indent=4))

    except requests.exceptions.RequestException as error:
        print(f"Could not communicate with microservice: {error}")
    except ValueError:
        print("The microservice returned an invalid JSON response.")


def main():
    """Test the sorting and filtering operations."""

    # Test 1: Sort sessions by date
    send_request("Sort by Date", {
        "operation": "sort",
        "field": "date",
        "order": "ascending",
        "records": sessions
    })

    # Test 2: Sort sessions by climbing grade
    send_request("Sort by Grade", {
        "operation": "sort",
        "field": "grade",
        "order": "ascending",
        "records": sessions
    })

    # Test 3: Filter sessions by location
    send_request("Filter by Location", {
        "operation": "filter",
        "field": "location",
        "value": "Movement",
        "records": sessions
    })


if __name__ == "__main__":
    main()
