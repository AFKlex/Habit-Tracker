import pytest
from datetime import datetime
from habit import habit
from habitManager import habitManager

# Test habit class
def test_habit_initialization():
    habit1 = habit("Exercise", "daily", "Morning workout", [], datetime(2023, 1, 1))
    assert habit1.name == "Exercise"
    assert habit1.frequency == "daily"
    assert habit1.description == "Morning workout"
    assert habit1.start_date == datetime(2023, 1, 1)
    assert habit1.check_dates == []

def test_add_check():
    habit1 = habit("Exercise", "daily", "Morning workout", [], datetime(2023, 1, 1))
    result = habit1.add_check(datetime(2023, 1, 2))
    assert result == "2023-01-02 successfully check"
    assert "2023-01-02" in habit1.check_dates

def test_add_duplicate_check():
    habit1 = habit("Exercise", "daily", "Morning workout", [], datetime(2023, 1, 1))
    habit1.add_check(datetime(2023, 1, 2))
    result = habit1.add_check(datetime(2023, 1, 2))
    assert result == "2023-01-02 is already checked."

def test_delete_check():
    habit1 = habit("Exercise", "daily", "Morning workout", ["2023-01-02"], datetime(2023, 1, 1))
    result = habit1.delete_check(datetime(2023, 1, 2))
    assert result == "2023-01-02 sucessfully removed from check"
    assert "2023-01-02" not in habit1.check_dates

def test_longest_streak():
    habit1 = habit("Exercise", "daily", "Morning workout", ["2023-01-01", "2023-01-02", "2023-01-03"], datetime(2023, 1, 1))
    result = habit1.longest_streak()
    assert result == "Exercise has the frequency daily and its longest streak is 3"

