
from hypothesis import given, strategies as st
from scholarship_awards import (
    parse_applicant,
    marks_average,
    payable_award
)

# Test 1: parse_applicant
@given(st.one_of(st.text(), st.none()))
def test_parse_applicant_no_crash(s):
    try:
        parse_applicant(s)
    except Exception as e:
        assert False, f"parse_applicant crashed with input {s!r}: {e}"

# Test 2: marks_average
@given(st.one_of(st.text(), st.none()))
def test_marks_average_no_crash(s):
    try:
        marks_average(s)
    except Exception as e:
        assert False, f"marks_average crashed with input {s!r}: {e}"

# Test 3: payable_award
@given(st.one_of(st.text(), st.none()))
def test_payable_award_no_crash(s):
    try:
        payable_award(s)
    except Exception as e:
        assert False, f"payable_award crashed with input {s!r}: {e}"