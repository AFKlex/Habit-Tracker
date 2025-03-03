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
    #rprint(frequency)
    manager.getHabits(frequency)

@habitShell.command()
@click.option('-n', '--name', required=True, help="Provide the Name for the newly created habit.")
@click.option('-f','--frequency',required=True, default="daily", show_default=True,type=click.Choice(["weekly","daily"],case_sensitive=False) ,help="Provide the frequency of Habits to create.")
@click.option('-d', '--description', required=False, default="", help="Provide a description for the Habit.")
@click.option('-s', '--startdate', required=False, default=str(today.strftime("%Y-%m-%d")), help ="Provide a Start Date for the Habit.")
@click.option('--customDateFormat', required=False, default="%Y-%m-%d", help="Provide a Custom Date formate to add a Date (default: %Y-%m-%d)")
def createHabit(name,frequency,description,startdate,customdateformat):
    manager.createHabit(name,frequency,description,manager.validateDate(startdate,customdateformat))

if __name__=='__main__':
    habitShell()
