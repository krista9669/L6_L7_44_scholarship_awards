import pytest

from scholarship_awards import application_status, award_amount, is_eligible


def test_award_amount_branch_paths():
    assert award_amount("merit", 75, "low", False) == 0
    assert award_amount("merit", 90, "high", False) == 900
    assert award_amount("merit", 90, "low", False) == 1500
    assert award_amount("merit", 90, "low", True) == 3200
    assert award_amount("sports", 70, "high", True) == 600
    assert award_amount("arts", 95, "low", False) == 4800


def test_award_amount_validation_edges():
    with pytest.raises(ValueError, match="unknown category"):
        award_amount("unknown", 80, "low", False)

    with pytest.raises(ValueError, match="invalid marks"):
        award_amount("merit", -1, "low", False)


def test_is_eligible_branch_paths():
    assert is_eligible(95, 1, False) is True
    assert is_eligible(70, 0, False) is False
    assert is_eligible(80, 2, True) is True
    assert is_eligible(80, 3, True) is False
    assert is_eligible(90, 2, True) is True
    assert is_eligible(90, 3, True) is False


def test_application_status_branch_paths():
    assert application_status(25, False, False) == "open"
    assert application_status(15, False, False) == "closing"
    assert application_status(4, False, False) == "closed"
    assert application_status(45, True, False) == "open"
    assert application_status(20, True, False) == "closing"
    assert application_status(10, True, False) == "closed"
    assert application_status(45, False, True) == "open"
    assert application_status(25, False, True) == "closing"
    assert application_status(10, False, True) == "closed"
