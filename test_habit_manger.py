import pytest
from datetime import datetime
from habit import habit
from habitManager import habitManager

# Fixture to create a fresh instance of habitManager for each test
@pytest.fixture
def manager():
    return habitManager()

# Test habit creation in habitManager
def test_create_habit(manager):
    manager.create_habit("Exercise", "daily", "Morning workout", "2023-01-01")
    assert any(h.name == "Exercise" for h in manager.habits)

# Test checking a habit
def test_check_habit(manager):
    manager.create_habit("Exercise", "daily", "Morning workout", "2023-01-01")
    result = manager.check_habit("Exercise", "2023-01-02", "%Y-%m-%d")
    assert "successfully check" in result

# Test deleting a habit
def test_delete_habit(manager):
    manager.create_habit("Exercise", "daily", "Morning workout", "2023-01-01")
    manager.delete_habit("Exercise")
    assert not any(h.name == "Exercise" for h in manager.habits)

