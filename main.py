import click
from click_shell import shell
from habitManager import *

#p1=habit("hi","bb")
#print(p1)

# Load Manager upon start of program
manager = habitManager()

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
@click.option('-f','--frequency',required=True, default="all", show_default=True,type=click.Choice(["weekly","daily"],case_sensitive=False) ,help="Provide the frequency of Habits to create.")
@click.option('-d', '--description', required=False, default="", help="Provide a description for the Habit.")
@click.option('-s', '--startdate', required=False, default="", help ="Provide a Start Date for the Habit.")
def createHabit(name,frequency,description,startdate):
    manager.createHabit(name,frequency,description,startdate)

if __name__=='__main__':
    habitShell()
