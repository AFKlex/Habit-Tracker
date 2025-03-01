import json
from habit_json import *
class habit:
    def __init__(self,name, frequency, description, checkDates,startDate):
        self.name = name
        self.frequency = frequency
        self.description =  description
        self.checkDates =  checkDates
        self.startDate = startDate

    def __str__(self):
        return f"Name: {self.name} \n\t-frequency: {self.frequency}\n\t-{self.description}\n\t-{self.startDate}\n\t-{self.checkDates}\n"


def getHabits():
    jsonData = readHabitData()
    #print(jsonData)

    habits = []
    for entry in jsonData:
        print(f"Entry: {entry}")
        habits.append(habit(entry["name"],entry["frequency"],entry["description"],entry["check_dates"],entry["start_date"]))

    for entry in habits:
        print(entry)
getHabits()
