import pytest

from scholarship_awards import application_status, award_amount, is_eligible


def test_award_amount_below_cutoff_returns_zero():
    assert award_amount("merit", 70, "low", False) == 0


def test_award_amount_low_income_uses_low_rate():
    assert award_amount("merit", 90, "low", False) == 1500


def test_award_amount_high_income_renewal_adjustment():
    assert award_amount("merit", 90, "high", True) == 2000


def test_award_amount_sports_renewal_keeps_sports_cutoff():
    assert award_amount("sports", 70, "low", True) == 1000


def test_award_amount_rejects_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        award_amount("unknown", 80, "low", False)


def test_award_amount_rejects_negative_marks():
    with pytest.raises(ValueError, match="invalid marks"):
        award_amount("merit", -1, "low", False)


def test_is_eligible_regular_student():
    assert is_eligible(90, 0, False) is True
    assert is_eligible(80, 2, False) is False


def test_is_eligible_special_quota_student():
    assert is_eligible(75, 2, True) is True
    assert is_eligible(75, 3, True) is False


def test_application_status_values():
    assert application_status(25, False, False) == "open"
    assert application_status(15, False, True) == "closing"
    assert application_status(5, True, False) == "closed"
