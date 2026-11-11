# LAB 7 – Fuzz Testing for Input Validation Bugs

## About

This lab explores fuzz testing as a software testing and security technique using the **Hypothesis** library in Python.

The Scholarship Awards application contains three functions that process applicant information, calculate average marks, and determine payable scholarship awards.

Hypothesis is used to automatically generate random and unexpected inputs to identify input validation bugs, crashes, and edge cases. The application is then improved using defensive programming and input validation.

## Objectives

- Understand the purpose and methodology of fuzz testing.
- Apply property-based testing using Hypothesis.
- Identify bugs caused by unexpected and malformed inputs.
- Improve application robustness through defensive programming.
- Verify the fixes by rerunning the fuzz tests.

## Technologies Used

- Python 3.12
- Hypothesis
- Pytest

## Project Structure

```text
LAB7/
│
├── scholarship_awards.py
├── test_scholarship_awards.py
├── README.md
│
└── screenshots/
    ├── 01_original_output.png
    ├── 02_fuzz_testing_failures.png
    ├── 03_fixed_application.png
    └── 04_final_tests_passed.png
```

## Application Functions

The application consists of three functions:

| Function | Description |
|---|---|
| `parse_applicant()` | Parses applicant category and marks. |
| `marks_average()` | Calculates the average of marks provided as comma-separated values. |
| `payable_award()` | Calculates the payable scholarship amount after applying an 18% increase and deduction. |

## Installation

Install the required dependencies:

```bash
pip install hypothesis
pip install pytest
```

## Execution

Run the original or fixed application:

```bash
python scholarship_awards.py
```

Run the Hypothesis fuzz tests:

```bash
python -m pytest test_scholarship_awards.py -v
```

## Fuzz Testing

Hypothesis was used to generate random strings and `None` values to test all three application functions.

The initial fuzz testing revealed several issues:

- Missing separators in input strings.
- Empty applicant categories and marks.
- Invalid numeric values.
- Empty CSV input.
- Unexpected `None` values.
- Incorrectly formatted award and deduction inputs.

These inputs caused exceptions such as `ValueError` and `AttributeError`.

## Bug Fixes and Improvements

The application was hardened using:

- Input type validation.
- Separator and field-count validation.
- Empty input checks.
- Exception handling for invalid numeric conversions.
- Finite-number validation for floating-point inputs.
- Safe handling of unexpected inputs.

Invalid inputs now return `None` instead of causing the application to crash.

## Test Results

**Initial Testing:**

All three Hypothesis tests failed, exposing input validation bugs in the original application.

**After Fixing:**

All three tests passed successfully:

| Test Case | Result |
|---|---|
| `test_parse_applicant_no_crash` | PASSED |
| `test_marks_average_no_crash` | PASSED |
| `test_payable_award_no_crash` | PASSED |

Final test execution:

```text
3 passed
```

## Conclusion

The lab demonstrated how property-based fuzz testing with Hypothesis can identify unexpected input validation bugs that may not be detected through ordinary testing.

By analysing the failing test cases and implementing defensive programming techniques, the Scholarship Awards application was made more robust against malformed and unexpected inputs.

The final fuzz testing confirmed that all three functions handled the generated test inputs without raising exceptions.