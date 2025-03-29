import json
from habit import *
from datetime import datetime
import click

class habitManager():
    """ This class manages is used to mange multiple habits. 
    It works as the main logic of the program.  
    """
    habits = []
    file_Path = "habit.json"
    #def __init__(self):
    #    self.load_saved_habits()

    def load_saved_habits(self):
        """This function loads all habits from a json file and create habit objects of the json data."""
        try:
            with open(self.file_Path, 'r') as file:
                habits_list = json.load(file)  # Load the entire JSON content

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
            return None

        except FileNotFoundError as e:
            error_message = f"Error loading habits: {e}\nA new habit.json will be created instead!"
            return error_message

        except json.JSONDecodeError as e:
            error_message = f"Error decoding habits file: {e}"
            return error_message

        except Exception as e:
            error_message = f"Unexpected error: {e}"
            return error_message


    def get_habits(self, frequency:str):
        """This function gets the data for all habits that are stored in the habits manager and returns it to the caller."""
        value = []
        for entry in self.habits:
            if frequency == entry.frequency or frequency == "all":
                value.append(entry)
        return value       

    def change_habit_by_name(self,name:str,frequency:str,description:str,start_date:datetime,new_name,custom_date_format):
        """This functions allows to change a habit. 

        Hint: 
            1. In order to work the habit needs to be fined by the name.
            2. Everything that is be changed will be added entry in a dict. 
            3. This dict will be returned while the manger also holds the changed habits.

        """
        changes = {}
        for entry in self.habits:
            if entry.name == name:
                # Check what was changed and change it in the attribute. 
                if frequency != None:
                    changes["frequency"] = {"old":entry.frequency, "new": frequency}
                    entry.set_frequency(frequency)

                if description != None:
                    changes["description"] = {"old":entry.description, "new":description}
                    entry.set_description(description)

                if start_date != None:
                    changes["start_date"]= {"old":entry.start_date, "new":start_date}
                    entry.set_start_date(self.validate_date(start_date,custom_date_format))

                if new_name != None:
                    changes["name"] = {"old":entry.name, "new":new_name}
                    entry.set_name(new_name)
                self.store_habits()
                return changes
        return None


    def store_habits(self):
        """This function stores all habits in a json file."""
        habit_json_data = []
        for entry in self.habits:
            habit_json_data.append(entry.as_dict())

        with open(self.file_Path,'w') as fp:
            json.dump(habit_json_data,fp,indent =4)

    def create_habit(self,name:str, frequency:str, description:str, start_date:str):
        """This function allows us to create a habit. 

        Hint:
            1. Here it also ensured, that a name only occours once in the list of all arrays.  
        """
        new_habit = habit(name,frequency,description,[],start_date)

        # Check if habit with a same name already exist in the list 
        for entry in self.habits:
            if entry.name == new_habit.name:
                return None

        self.habits.append(new_habit)
        self.store_habits()
        return new_habit

    def delete_habit(self,name:str):
        """ This function deletes a habit by the name."""
        remove_status = False
        for entry in self.habits:
            if entry.name == name:
                self.habits.remove(entry)
                self.store_habits()
                remove_status = True
                break
        return remove_status

    def delete_all_habit(self):
        """This function deletes all habits in the habit manager"""
        self.habits = []
        self.store_habits()
        return "All habits deleted"

    def validate_date(self,date_string, date_format="%Y-%m-%d"):
        """ This function is used to validate if a date is a valid and defined format."""
        try:
            # Try to parse the date string according to the specified format
            parsed_date = datetime.strptime(date_string, date_format)
            # If successful, return the parsed date
            return parsed_date
        except ValueError:
            # If an exception occurs (invalid date), return None or handle accordingly
            return None

    def check_habit(self,name, date,custom_date_format):
        """ This function checks a habit by name"""
        for entry in self.habits:
            if entry.name == name:
                result = entry.add_check(self.validate_date(date,custom_date_format))
                self.store_habits()
                return result

    def delete_check(self,name,date,custom_date_format):
        """ This function deletes a check for a defined habit"""
        for entry in self.habits:
            if entry.name == name:
                result = entry.delete_check(self.validate_date(date,custom_date_format))
                self.store_habits()
                return result 

    def get_longest_streak(self, name):
        """ This function gets the longest streak for a defined habit or all habits"""
        data_to_return = []
        if name is None:
            for entry in self.habits:
                data_to_return.append(entry.longest_streak())
        else:
            for entry in self.habits:
                if entry.name == name:
                    data_to_return.append(entry.longest_streak())
        return data_to_return
