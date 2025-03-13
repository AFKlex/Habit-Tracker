import pytest
from habitManager import habitManager

# Fixture to create a fresh instance of habitManager for each test
@pytest.fixture
def manager():
    manager = habitManager()
    manager.load_saved_habits()
    return manager

# Test habit creation in habitManager
def test_create_habit(manager):
    date = manager.validate_date("2023-01-01", "%Y-%m-%d")
    manager.create_habit("Exercise", "daily", "Morning workout", date)
    assert any(h.name == "Exercise" for h in manager.habits)

# Test checking a habit
def test_check_habit(manager):
    date = manager.validate_date("2023-01-01", "%Y-%m-%d")
    manager.create_habit("Exercise", "daily", "Morning workout", date)
    result = manager.check_habit("Exercise", "2023-01-02", "%Y-%m-%d")
    assert "successfully check" in result

# Test deleting a habit
def test_delete_habit(manager):
    date = manager.validate_date("2023-01-01", "%Y-%m-%d")
    manager.create_habit("Exercise", "daily", "Morning workout", date)
    manager.delete_habit("Exercise")
    assert not any(h.name == "Exercise" for h in manager.habits)

