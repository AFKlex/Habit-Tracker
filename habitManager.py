import json
from habit import *
from datetime import datetime
import click
class habitManager():
    habits = []
    filePath = "habit.json"
    def __init__(self):
        self.loadSavedHabits()

    def loadSavedHabits(self):
        try:
            with open(self.filePath, 'r') as file:
                data = json.load(file)  # Load the entire JSON content

            # Ensure the "habits" key exists
            habits_list = data

            # Initialize self.habits
            self.habits = [
                habit(
                    entry["name"],
                    entry["frequency"],
                    entry["description"],
                    entry["checkDates"],
                    self.validateDate(entry["startDate"],"%Y-%m-%d")
                )
                for entry in habits_list
            ]

            #print(self.habits)  # Debugging

        except (FileNotFoundError, json.JSONDecodeError) as e:
            click.secho(f"Error loading habits: {e}\nA new habit.json will be created instead!",fg="red")

    def getHabits(self, frequency:str):
        for entry in self.habits:
            #print(f"frequency {frequency} entry.freqency {entry.frequency}")
            if frequency == entry.frequency or frequency == "all":
                click.secho(entry,fg="blue")

    def changeHabitByName(self,name:str,frequency:str,description:str,startDate:datetime,newName,customDateFormat):
        for entry in self.habits:
            if entry.name == name:
                if frequency != None:
                    entry.setFrequency(frequency)

                if description != None:
                    entry.setDescription(description)

                if startDate != None:
                    entry.setStartDate(self.validateDate(startDate,customDateFormat))

                if newName != None:
                    entry.setName(newName)
                self.storeHabits()
                break


    def storeHabits(self):
        habitJsonData = []
        for entry in self.habits:
            habitJsonData.append(entry.asDict())
        #print(habitJsonData)
        with open(self.filePath,'w') as fp:
            json.dump(habitJsonData,fp,indent =4)

    def createHabit(self,name:str, frequency:str, description:str, startDate:str):
        newHabit = habit(name,frequency,description,[],startDate)

        # Check if habit with a same name already exist in the list 
        for entry in self.habits:
            if entry.name == newHabit.name:
                click.secho(f'"{newHabit.name}" already exist in habit list, try alter the name or modify the existing habit!',fg="red")
                return 1

        self.habits.append(newHabit)
        self.storeHabits()
        click.secho("Habit added successfully!",fg="green")

    def deleteHabit(self,name:str):
        removeStatus = False
        for entry in self.habits:
            if entry.name == name:
                self.habits.remove(entry)
                self.storeHabits()
                removeStatus = True
                break
        if removeStatus:
            click.secho("Habit removed successfully",fg="green")
        else:
            click.secho("Habit could not be found! Try checking the Name.",fg="red")


    def validateDate(self,date_string, date_format="%Y-%m-%d"):
        try:
            # Try to parse the date string according to the specified format
            parsed_date = datetime.strptime(date_string, date_format)
            # If successful, return the parsed date
            return parsed_date
        except ValueError:
            # If an exception occurs (invalid date), return None or handle accordingly
            return None

