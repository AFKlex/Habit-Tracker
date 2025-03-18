#!./venv3/bin/python3
import click
from click_shell import shell
from habitManager import *
from datetime import date
from habit import * 

# Load Manager upon start of program
manager = habitManager()
error_message = manager.load_saved_habits()
if error_message: 
    click.secho(error_message,fg="red")
today= date.today()

@shell(prompt='Habit >', intro='Welcome to simple Habit Shell!')
def habitShell():
    """Initialize the habit shell CLI.
    
    Hint:
        1. This function sets up the interactive shell for managing habits.
    """
    pass

@habitShell.command()
@click.option('-f','--frequency',required=False, default="all", show_default=True,type=click.Choice(["weekly","daily","all"],case_sensitive=False) ,help="Provide a Filter for the frequency of Habits to get.")
def getHabits(frequency):
    """Retrieve and display habits based on frequency.
    
    Hint:
        1. This function fetches habits from the manager based on the given frequency filter.
    """
    habits_to_print = manager.get_habits(frequency)
    for entry in habits_to_print: 
        click.secho(entry,fg="blue")


@habitShell.command()
@click.option('-n', '--name', required=True, help="Provide the Name for the newly created habit.")
@click.option('-f','--frequency',required=True, default="daily", show_default=True,type=click.Choice(["weekly","daily"],case_sensitive=False) ,help="Provide the frequency of Habits to create.")
@click.option('-d', '--description', required=False, default="", help="Provide a description for the Habit.")
@click.option('-s', '--startdate', required=False, default=str(today.strftime("%Y-%m-%d")), help ="Provide a Start Date for the Habit.")
@click.option('--customDateFormat', required=False, default="%Y-%m-%d", help="Provide a Custom Date formate to add a Date (default: %Y-%m-%d)")
def createHabit(name,frequency,description,startdate,customdateformat):
    """Create a new habit.
    
    Hint:
        1. This function adds a new habit to the manager with the given parameters.
    """
    status = manager.create_habit(name,frequency,description,manager.validate_date(startdate,customdateformat))

    if status is None: 
        click.secho(f"{name} already exist in habit list, try alter the name or modify the existing habit!", fg="red")
    else:
        click.secho(f"Habit added successfully!",fg="green")

@habitShell.command()
@click.option('-n', '--name', required=True, help="Provide the Name for the habit to change.")
@click.option('-f','--frequency',required=False, default=None, show_default=True,type=click.Choice(["weekly","daily"],case_sensitive=False) ,help="Change the frequency of the habit.")
@click.option('-d', '--description', required=False, default=None, help="Change the description of the habit")
@click.option('-s', '--startdate', required=False, default=None, help ="Change the start Date of the habit.")
@click.option('-N', '--newName', required=False, default=None, help="Change the name of a Habit")
@click.option('--customDateFormat', required=False, default="%Y-%m-%d", help="Provide a Custom Date formate to add a Date (default: %Y-%m-%d)")
def changeHabit(name,frequency,description,startdate,newname,customdateformat):
    """Modify an existing habit.
    
    Hint:
        1. This function updates the details of a habit based on the provided parameters.
    """
    changes = manager.change_habit_by_name(name,frequency,description,startdate,newname,customdateformat)

    if not changes:
        click.secho("No changes or habit not found.",fg="red")
    
    click.secho("Changes made:",fg="bright_black")
    for key, value in changes.items():
        click.secho(f"\t{key.capitalize()}: {value['old']} -> {value['new']}",fg="bright_black")

@habitShell.command()
@click.option('-n', '--name', required=True, help="Provide the name for the habit to delete.")
def deleteHabit(name):
    """Delete a habit by name.
    
    Hint:
        1. This function removes a habit from the manager.
    """
    status = manager.delete_habit(name)

    if status: 
        click.secho("Habit removed successfully",fg="green")
    else:
        click.secho("Habit could not be found! Try checking the Name",fg="red")

@habitShell.command()
def deleteAllHabit():
    """Delete all habits.
    
    Hint:
        1. This function clears all stored habits.
    """
    status= manager.delete_all_habit()
    click.secho(status,fg="green")

@habitShell.command()
@click.option('-n', '--name', required=True, help="Provide the Name for the habit to check.")
@click.option('-d', '--date', required=False, default=str(today.strftime("%Y-%m-%d")), help ="Change the date of the habit to check.")
@click.option('--customDateFormat', required=False, default="%Y-%m-%d", help="Provide a Custom Date formate to add a Date (default: %Y-%m-%d)")
def checkHabit(name,date,customdateformat):
    """Mark a habit as checked for a specific date.
    
    Hint:
        1. This function records a habit completion for a given date.
    """
    result = manager.check_habit(name,date,customdateformat)
    click.secho(result,fg="bright_black")

@habitShell.command()
@click.option('-n', '--name', required=True, help="Provide the Name for the habit to check.")
@click.option('-d', '--date', required=False, default=str(today.strftime("%Y-%m-%d")), help ="Change the date of the habit to check.")
@click.option('--customDateFormat', required=False, default="%Y-%m-%d", help="Provide a Custom Date formate to add a Date (default: %Y-%m-%d)")
def deletecheck(name,date,customdateformat):
    result = manager.delete_check(name,date,customdateformat)
    click.secho(result, fg="bright_black")

@habitShell.command()
@click.option('-n', '--name', required=False, default=None, help="Provide the Name to check the longest streak for a single Habit.")
def getLongestStreak(name):
    """Get the longest streak of a habit.
    
    Hint:
        1. This function retrieves the longest completion streak for a specific habit.
    """
    result = manager.get_longest_streak(name)
    for entry in result:
        click.secho(entry,fg="green")

if __name__=='__main__':
    habitShell()
