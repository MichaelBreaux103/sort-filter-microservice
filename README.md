# Sort & Filter Microservice

## Description

This microservice was created for CS361 Software Engineering I. It sorts and filters records for the Climbing Progression Tracker and Task Tracker applications.

The microservice uses Python and Flask to receive HTTP requests, process records, and return the results in JSON format.

## Features

- Sort climbing sessions by date.
- Sort climbing sessions by grade (V2, V5, V10, etc.).
- Filter climbing sessions by a specified field, such as location.
- Return processed records in JSON format.
- Return an HTTP 400 error for invalid operations.

## Requirements

- Python 3
- Flask
- Requests (for the testing program)

Install the required libraries:

```bash
python3 -m pip install flask requests
```

## Running the Microservice

Open a terminal in the `sort-filter-microservice` folder and run:

```bash
python3 sort_filter_service.py
```

The microservice starts a local Flask server at:

`http://127.0.0.1:5001`

Keep this terminal running while sending requests.

## Communication

The microservice uses HTTP requests and JSON to communicate with other programs.

**Endpoint:** `POST /process`

**Base URL:** `http://127.0.0.1:5001`

### Example: Sort by Grade

Send the following JSON request:

```json
{
  "operation": "sort",
  "field": "grade",
  "order": "ascending",
  "records": [
    {"date": "2026-11-03", "grade": "V10", "location": "The Spot"},
    {"date": "2026-11-08", "grade": "V5", "location": "Movement"},
    {"date": "2026-11-06", "grade": "V2", "location": "Movement"}
  ]
}
```

**Example response:**

```json
{
  "records": [
    {"date": "2026-11-06", "grade": "V2", "location": "Movement"},
    {"date": "2026-11-08", "grade": "V5", "location": "Movement"},
    {"date": "2026-11-03", "grade": "V10", "location": "The Spot"}
  ]
}
```

### Example: Filter by Location

```json
{
  "operation": "filter",
  "field": "location",
  "value": "Movement",
  "records": [
    {"date": "2026-11-03", "grade": "V10", "location": "The Spot"},
    {"date": "2026-11-08", "grade": "V5", "location": "Movement"}
  ]
}
```

**Example response:**

```json
{
  "records": [
    {"date": "2026-11-08", "grade": "V5", "location": "Movement"}
  ]
}
```

## Testing

With the microservice running, open a second terminal and enter:

```bash
python3 test_sort_filter.py
```

The testing program demonstrates sorting by date, sorting by grade, and filtering by location.

Successful requests return HTTP status code `200`.

Invalid operations return HTTP status code `400`.

## Files

- `sort_filter_service.py` — Flask microservice implementation.
- `test_sort_filter.py` — Program used to test the microservice.
- `README.md` — Instructions and documentation.
- `.gitignore` — Specifies files Git should ignore.
