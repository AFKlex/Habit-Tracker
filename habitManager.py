import json
from habit import *
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
                    entry["startDate"]
                )
                for entry in habits_list
            ]

            #print(self.habits)  # Debugging

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading habits: {e}")

    def getHabits(self, frequency:str):
        for entry in self.habits:
            print(f"frequency {frequency} entry.freqency {entry.frequency}")
            if frequency == entry.frequency or frequency == "all":
                print(entry)



    def createHabit(self,name:str, frequency:str, description:str, startDate:str):
        newHabit = habit(name,frequency,description,[],startDate)

        self.habits.append(newHabit)

        habitJsonData = []
        for entry in self.habits:
            habitJsonData.append(entry.__dict__)
        print(habitJsonData)
        with open(self.filePath,'w') as fp:
            json.dump(habitJsonData,fp,indent =4)

