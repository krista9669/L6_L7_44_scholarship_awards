# L6 & L7 – Software Engineering Laboratory

**Repository:** L6_L7_44_scholarship_awards

This repository contains the implementations and testing activities completed as part of Lab 6 and Lab 7 for the Software Engineering Laboratory.

Both labs use the Scholarship Awards application to explore different software testing techniques, focusing on code coverage, branch coverage, and fuzz testing.

---

# Lab 6 – Code Coverage and Branch Coverage

## 1. About

Lab 6 focuses on evaluating software test quality using code coverage and branch coverage techniques.

The objective is to design and execute test cases that exercise different statements, conditions, and decision branches in the Scholarship Awards application.

Coverage reports are used to identify untested statements and conditional branches and evaluate the effectiveness of the test suite.

## 2. Objectives

- Understand code coverage and branch coverage.
- Identify executable statements and decision branches.
- Design test cases for different execution paths.
- Identify untested statements and conditional branches.
- Improve test coverage through additional test cases.
- Evaluate test effectiveness using coverage reports.

## 3. Technologies Used

- Python
- Pytest
- Coverage.py / pytest-cov
- Visual Studio Code

## 4. Testing Approach

### Code Coverage

Code coverage measures how much of the application's executable code is executed when the test suite runs.

The objective is to ensure that relevant statements across the application are exercised.

### Branch Coverage

Branch coverage measures whether the different outcomes of conditional statements are executed.

Test cases are designed to exercise different decision paths, including true and false outcomes wherever applicable.

## 5. Project Files

| File | Description |
|---|---|
| `scholarship_awards.py` | Scholarship Awards application |
| `test_scholarship_awards.py` | Application test file |
| `CodeCoverageTest_...py` | Code coverage test implementation |
| `BranchCoverageTest_...py` | Branch coverage test implementation |
| `CodeCoverage_...png` | Code coverage screenshot |
| `BranchCoverage_...png` | Branch coverage screenshot |
| `PES2UG24CS234_Lab6_CodeBranchCoverage.pdf` | Lab 6 documentation and results |

## 6. Execution

Run the application:

```bash
python scholarship_awards.py
```

Run the test suite:

```bash
python -m pytest -v
```

Generate a coverage report, if pytest-cov is configured:

```bash
python -m pytest --cov=scholarship_awards --cov-report=term-missing
```

## 7. Conclusion

Lab 6 demonstrated the importance of code coverage and branch coverage in evaluating software testing effectiveness.

The exercise highlighted that successful program execution does not necessarily mean all statements and decision paths have been adequately tested. Both coverage techniques help develop a more comprehensive test suite.

---

# Lab 7 – Fuzz Testing for Input Validation Bugs

## 1. About

Lab 7 explores fuzz testing as a software testing and security technique using the Hypothesis library in Python.

The Scholarship Awards application contains three functions that process applicant information, calculate average marks, and determine payable scholarship amounts.

Hypothesis is used to automatically generate random and unexpected inputs to identify input validation bugs, runtime exceptions, and edge cases.

The identified issues are addressed using defensive programming and input validation techniques to improve application robustness.

## 2. Objectives

- Understand the purpose and methodology of fuzz testing.
- Apply property-based testing using Hypothesis.
- Identify bugs caused by unexpected and malformed inputs.
- Analyse failures discovered through automatically generated test cases.
- Improve application robustness through input validation.
- Verify fixes by rerunning the fuzz tests.

## 3. Technologies Used

- Python 3.12.7
- Hypothesis
- Pytest
- Visual Studio Code

## 4. Application Functions

The application contains three main functions:

| Function | Description |
|---|---|
| `parse_applicant(text)` | Parses applicant category and marks from a colon-separated input. |
| `marks_average(marks_csv)` | Calculates the average of comma-separated marks. |
| `payable_award(text)` | Calculates the payable scholarship amount after an 18% increase and deduction. |

### Sample Inputs and Outputs

**parse_applicant()**

Input:
```python
merit:82
```

Output:
```python
('Merit', 82.0)
```

**marks_average()**

Input:
```python
72,85,90
```

Output:
```python
82
```

**payable_award()**

Input:
```python
5000|500
```

Output:
```python
5400.0
```

## 5. Installation

Install the required dependencies:

```bash
pip install hypothesis
pip install pytest
```

## 6. Fuzz Testing Implementation

Hypothesis was used to generate unexpected inputs for all three application functions.

The following strategies were used:

- `st.text()` – Generates random strings.
- `st.none()` – Generates None values.
- `st.one_of()` – Combines multiple input strategies.
- `@given()` – Supplies automatically generated inputs to test functions.

Three fuzz tests were implemented:

1. `test_parse_applicant_no_crash()`
2. `test_marks_average_no_crash()`
3. `test_payable_award_no_crash()`

## 7. Bugs Identified

Initial fuzz testing exposed input validation issues in all three functions.

| Function | Unexpected Input | Identified Issue |
|---|---|---|
| `parse_applicant()` | `None` | AttributeError |
| `parse_applicant()` | Empty string | ValueError |
| `parse_applicant()` | `:` | Invalid numeric conversion |
| `marks_average()` | `None` | AttributeError |
| `marks_average()` | Empty string | ValueError |
| `payable_award()` | `None` | AttributeError |
| `payable_award()` | Empty string | ValueError |
| `payable_award()` | `|` | Invalid numeric conversion |

## 8. Bug Fixes and Improvements

The application was improved using:

- Input type validation.
- Separator and field-count validation.
- Empty input checks.
- Exception handling for invalid numeric conversions.
- Finite-number validation using `math.isfinite()`.
- Safe return values for invalid inputs.

Invalid inputs now return `None` instead of causing unexpected exceptions.

## 9. Execution

Run the application:

```bash
python scholarship_awards.py
```

Run the fuzz tests:

```bash
python -m pytest test_scholarship_awards.py -v
```

## 10. Testing Results

### Initial Testing – Before Fixing

All three Hypothesis tests failed, exposing input validation bugs.

```text
test_parse_applicant_no_crash FAILED
test_marks_average_no_crash FAILED
test_payable_award_no_crash FAILED

3 failed
```

### Final Testing – After Fixing

After implementing input validation and defensive programming, all three tests passed.

```text
test_parse_applicant_no_crash PASSED
test_marks_average_no_crash PASSED
test_payable_award_no_crash PASSED

3 passed
```

## 11. Conclusion

Lab 7 demonstrated how property-based fuzz testing with Hypothesis can identify unexpected input validation bugs that may not be detected through ordinary testing.

By analysing failing test cases and implementing defensive programming techniques, the Scholarship Awards application was made more robust against malformed and unexpected inputs.

The final test execution confirmed that all three functions handled the generated inputs without raising unexpected exceptions.

---

# Overall Conclusion

Lab 6 and Lab 7 demonstrate two complementary approaches to software testing.

- **Lab 6:** Focuses on measuring test effectiveness through code coverage and branch coverage.
- **Lab 7:** Focuses on identifying unexpected input-related bugs through automated fuzz testing.

Together, these exercises demonstrate the importance of comprehensive testing, input validation, and defensive programming in developing reliable software applications.