# FastBox Mystery Delivery System

## Project Overview

This project simulates a one-day delivery operation for a fictional logistics company called FastBox.

The system:

- Reads warehouse, agent, and package data from JSON files
- Assigns each package to the nearest delivery agent
- Calculates delivery distances using Euclidean Distance
- Tracks agent performance
- Identifies the most efficient delivery agent
- Generates a delivery report in JSON format

---

## Features

✅ JSON Parsing

✅ Nearest Agent Assignment

✅ Euclidean Distance Calculation

✅ Delivery Simulation

✅ Agent Statistics Generation

✅ Best Agent Identification

✅ Report Export to report.json

✅ Works with base_case.json

✅ Works with all provided test cases

---

## Technologies Used

- Python 3
- JSON
- Math Module

---

## Project Structure

```text
fastbox_assignment/
│
├── delivery_system.py
├── base_case.json
├── report.json
├── README.md
│
└── test_cases/
    ├── test_case_1.json
    ├── test_case_2.json
    ├── test_case_3.json
    ├── test_case_4.json
    ├── test_case_5.json
    ├── test_case_6.json
    ├── test_case_7.json
    ├── test_case_8.json
    ├── test_case_9.json
    └── test_case_10.json
```

---

## Assignment Workflow

### Step 1

Load data from JSON file.

Example:

```python
with open(filename, "r") as file:
    data = json.load(file)
```

---

### Step 2

Find nearest agent for each package.

Distance Formula:

```text
distance =
√((x₂ - x₁)² + (y₂ - y₁)²)
```

---

### Step 3

Assign package to nearest agent.

Example:

```text
Package P1 → Agent A1
Package P2 → Agent A2
Package P3 → Agent A3
```

---

### Step 4

Calculate delivery distance.

Total Distance:

```text
Agent → Warehouse
+
Warehouse → Destination
```

---

### Step 5

Generate agent statistics.

Example:

```json
{
    "A1": {
        "packages_delivered": 2,
        "total_distance": 78.28,
        "efficiency": 39.14
    }
}
```

---

### Step 6

Find Best Agent.

Formula:

```text
efficiency =
total_distance / packages_delivered
```

Lower efficiency value indicates better performance.

---

## Running the Project

Run with base case:

```bash
python delivery_system.py
```

Example input:

```text
base_case.json
```

---

## Testing

The project has been tested using:

- Base Case
- Test Case 1
- Test Case 2
- Test Case 3
- Test Case 4
- Test Case 5
- Test Case 6
- Test Case 7
- Test Case 8
- Test Case 9
- Test Case 10

Total Test Cases: 11

---

## Sample Output

```json
{
    "assignments": [
        {
            "package_id": "P1",
            "agent_id": "A1",
            "distance": 57.07
        }
    ],
    "agent_statistics": {
        "A1": {
            "packages_delivered": 2,
            "total_distance": 78.28,
            "efficiency": 39.14
        }
    },
    "best_agent": "A3"
}
```

---

## Evaluation Criteria Covered

| Criteria | Status |
|-----------|---------|
| JSON Parsing | ✅ |
| Distance Calculation | ✅ |
| Agent Assignment | ✅ |
| Simulation | ✅ |
| Report Generation | ✅ |
| Code Clarity | ✅ |
| Multiple Test Cases | ✅ |

---

## Author

Gourav Tambulkar

AI / ML Developer

Python Developer

Generative AI Enthusiast