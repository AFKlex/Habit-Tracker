from habit import *
import click 
from click_shell import shell 

#p1=habit("hi","bb")
#print(p1)

@shell(prompt='Habit >', intro='Welcome to simple Habit Shell!')
def habitShell():
    pass

@habitShell.command()
@click.option('-f','--frequency',required=False, default="all", show_default=True,type=click.Choice(["weekly","daily","all"],case_sensitive=False) ,help="Provide a Filter for the frequency of Habits to get.")
def getHabit(frequency):
    #print(frequency)
    getHabits()

if __name__=='__main__':
    habitShell()
