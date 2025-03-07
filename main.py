#!./venv3/bin/python3
import click
from click_shell import shell
from habitManager import *
from datetime import date

# Load Manager upon start of program
manager = habitManager()
today= date.today()


@shell(prompt='Habit >', intro='Welcome to simple Habit Shell!')
def habitShell():
    pass

@habitShell.command()
@click.option('-f','--frequency',required=False, default="all", show_default=True,type=click.Choice(["weekly","daily","all"],case_sensitive=False) ,help="Provide a Filter for the frequency of Habits to get.")
def getHabits(frequency):
    manager.get_habits(frequency)

@habitShell.command()
@click.option('-n', '--name', required=True, help="Provide the Name for the newly created habit.")
@click.option('-f','--frequency',required=True, default="daily", show_default=True,type=click.Choice(["weekly","daily"],case_sensitive=False) ,help="Provide the frequency of Habits to create.")
@click.option('-d', '--description', required=False, default="", help="Provide a description for the Habit.")
@click.option('-s', '--startdate', required=False, default=str(today.strftime("%Y-%m-%d")), help ="Provide a Start Date for the Habit.")
@click.option('--customDateFormat', required=False, default="%Y-%m-%d", help="Provide a Custom Date formate to add a Date (default: %Y-%m-%d)")
def createHabit(name,frequency,description,startdate,customdateformat):
    manager.create_habit(name,frequency,description,manager.validate_date(startdate,customdateformat))

@habitShell.command()
@click.option('-n', '--name', required=True, help="Provide the Name for the habit to change.")
@click.option('-f','--frequency',required=False, default=None, show_default=True,type=click.Choice(["weekly","daily"],case_sensitive=False) ,help="Change the frequency of the habit.")
@click.option('-d', '--description', required=False, default=None, help="Change the description of the habit")
@click.option('-s', '--startdate', required=False, default=None, help ="Change the start Date of the habit.")
@click.option('-N', '--newName', required=False, default=None, help="Change the name of a Habit")
@click.option('--customDateFormat', required=False, default="%Y-%m-%d", help="Provide a Custom Date formate to add a Date (default: %Y-%m-%d)")
def changeHabit(name,frequency,description,startdate,newname,customdateformat):
    manager.change_habit_by_name(name,frequency,description,startdate,newname,customdateformat)

@habitShell.command()
@click.option('-n', '--name', required=True, help="Provide the name for the habit to delete.")
def deleteHabit(name):
    manager.delete_habit(name)

@habitShell.command()
def deleteAllHabit():
    manager.delete_all_habit()

if __name__=='__main__':
    habitShell()
