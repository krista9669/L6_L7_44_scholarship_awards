# Lab 6: Code and Branch Coverage

## Student Details

**Name:** KRISHITHA KANKANALA  
**SRN:** PES2UG24CS234

---

## Overview

This lab focuses on writing and improving test cases for a Python scholarship award system. The goal is to achieve strong code and branch coverage by validating the core business rules in the module.

The project checks:

- scholarship award calculation by category and marks
- income-based award adjustments
- renewal-specific eligibility logic
- applicant eligibility based on attendance, backlog count, and special quota rules
- application status based on days remaining and application type

---

## Project Files

| File | Description |
|------|-------------|
| `scholarship_awards.py` | Python module containing the scholarship logic |
| `test_scholarship_awards.py` | Starter test file for coverage-based validation |
| `CodeCoverageTest_PES2UG24CS234_application.py` | Coverage-driven test script |
| `BranchCoverageTest_PES2UG24CS234_application.py` | Branch coverage test script |
| `CodeCoverage_PES2UG24CS234.png` | Code coverage report image |
| `BranchCoverage_PES2UG24CS234.png` | Branch coverage report image |
| `PES2UG24CS234_Lab6_CodeBranchCoverage.pdf` | Final submission report PDF |

---

## Core Functionality

The module contains the following functions:

- `award_amount(category, marks, income_level, is_renewal)`
  - Computes the scholarship amount based on the category, marks achieved, income level, and whether the award is a renewal.
- `is_eligible(attendance, backlogs, is_special_quota)`
  - Checks whether an applicant meets eligibility rules.
- `application_status(days_left, is_renewal, is_paper)`
  - Returns the application state as `open`, `closing`, or `closed`.

---

## Objectives

This lab requires students to:

1. Analyze the rules implemented in the module.
2. Add meaningful test cases for normal and edge cases.
3. Improve code coverage to a high level.
4. Ensure both branch coverage and statement coverage are considered.
5. Validate that the logic behaves correctly for valid and invalid input conditions.

---

## How to Run

Create a virtual environment if needed, then install pytest:

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
# or
venv\Scripts\activate       # Windows
pip install pytest pytest-cov
```

Run the tests:

```bash
pytest -q
```

Run coverage checks:

```bash
pytest --cov=scholarship_awards --cov-report=term-missing
```

---

## Expected Outcome

The final implementation should provide a reliable set of tests covering:

- valid and invalid scholarship award calculations
- category validation errors
- mark-based thresholds and renewal conditions
- special quota and attendance/backlog rules
- application deadlines and closing/open states

This lab is intended to reinforce software testing principles, especially branch coverage and validation of condition-based logic.

---

## Notes

Keep all Lab 6 work in this folder, as noted in the course instructions. Lab 7 will be added to the repository at a later stage.
