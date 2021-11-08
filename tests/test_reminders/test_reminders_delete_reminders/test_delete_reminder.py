import pytest
from task_scheduler.reminder.reminder_handler import RemindersHandler

@pytest.fixture
def reminder_handler():
    rmh = RemindersHandler("./tests/test_reminders/reminder.csv")
    return rmh

def  test_delete_reminder_by_number_of_remaining_reminders(reminder_handler):
    expected = 1
    reminder_handler.delete_reminder(1)
    actual = len(reminder_handler.reminders)
    assert actual == expected
    
    
def test_delete_reminder_by_value_of_remaining_reminders(reminder_handler):
    expected = "First reminder"
    reminder_handler.delete_reminder(1)
    actual = reminder_handler.reminders.iloc[0]['message']
    assert actual == expected
    
