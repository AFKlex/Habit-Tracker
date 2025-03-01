import json


def readHabitData():
    with open("habit.json",'r') as file: 
        data = json.load(file)["habits"]
        return data


