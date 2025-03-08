import json
from habit import *
from datetime import datetime
import click
class habitManager():
    habits = []
    file_Path = "habit.json"
    def __init__(self):
        self.load_saved_habits()

    def load_saved_habits(self):
        try:
            with open(self.file_Path, 'r') as file:
                data = json.load(file)  # Load the entire JSON content

            # Ensure the "habits" key exists
            habits_list = data

            # Initialize self.habits
            self.habits = [
                habit(
                    entry["name"],
                    entry["frequency"],
                    entry["description"],
                    entry["check_dates"],
                    self.validate_date(entry["start_date"],"%Y-%m-%d")
                )
                for entry in habits_list
            ]


        except (FileNotFoundError, json.JSONDecodeError) as e:
            click.secho(f"Error loading habits: {e}\nA new habit.json will be created instead!",fg="red")

    def get_habits(self, frequency:str):
        for entry in self.habits:
            if frequency == entry.frequency or frequency == "all":
                click.secho(entry,fg="blue")

    def change_habit_by_name(self,name:str,frequency:str,description:str,start_date:datetime,new_name,custom_date_format):
        for entry in self.habits:
            if entry.name == name:
                if frequency != None:
                   click.secho(entry.set_frequency(frequency),fg="bright_black")

                if description != None:
                    click.secho(entry.set_description(description),fg="bright_black")

                if start_date != None:
                    click.secho(entry.set_start_date(self.validate_date(start_date,custom_date_format)),fg="bright_black")

                if new_name != None:
                    click.secho(entry.set_name(new_name),fg="bright_black")
                self.store_habits()
                break


    def store_habits(self):
        habit_json_data = []
        for entry in self.habits:
            habit_json_data.append(entry.as_dict())

        with open(self.file_Path,'w') as fp:
            json.dump(habit_json_data,fp,indent =4)

    def create_habit(self,name:str, frequency:str, description:str, start_date:str):
        new_habit = habit(name,frequency,description,[],start_date)

        # Check if habit with a same name already exist in the list 
        for entry in self.habits:
            if entry.name == new_habit.name:
                click.secho(f'"{new_habit.name}" already exist in habit list, try alter the name or modify the existing habit!',fg="red")
                return 1

        self.habits.append(new_habit)
        self.store_habits()
        click.secho("Habit added successfully!",fg="green")

    def delete_habit(self,name:str):
        remove_status = False
        for entry in self.habits:
            if entry.name == name:
                self.habits.remove(entry)
                self.store_habits()
                remove_status = True
                break
        if remove_status:
            click.secho("Habit removed successfully",fg="green")
        else:
            click.secho("Habit could not be found! Try checking the Name.",fg="red")

    def delete_all_habit(self):
        self.habits = []
        self.store_habits()

    def validate_date(self,date_string, date_format="%Y-%m-%d"):
        try:
            # Try to parse the date string according to the specified format
            parsed_date = datetime.strptime(date_string, date_format)
            # If successful, return the parsed date
            return parsed_date
        except ValueError:
            # If an exception occurs (invalid date), return None or handle accordingly
            return None

    def check_habit(self,name, date,custom_date_format):
        for entry in self.habits:
            if entry.name == name:
                entry.add_check(self.validate_date(date,custom_date_format))
                #print(entry)
                #print(entry.as_dict())
                self.store_habits()
                break
