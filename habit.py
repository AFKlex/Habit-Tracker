import json
from datetime import datetime
class habit:
    def __init__(self,name, frequency, description, check_dates,start_date:datetime):
        self.name = name.strip()
        self.frequency = frequency
        self.description =  description
        self.check_dates =  check_dates
        self.start_date = start_date
    def __str__(self):
        return f"Name: {self.name} \n\t- frequency: {self.frequency}\n\t- {self.description}\n\t- {self.start_date.strftime('%Y-%m-%d')}\n\t- {self.check_dates}\n"

    def as_dict(self):
        return {
            "name":self.name,
            "frequency":self.frequency,
            "description":self.description,
            "check_dates": self.check_dates,
            "start_date":self.start_date.strftime("%Y-%m-%d")
        }
    def set_name(self,name:str):
        self.name = name
        return "Name set successfully"

    def set_frequency(self,frequency:str):
        if frequency == "weekly" or frequency == "daily":
            self.frequency = frequency
            return "Frequency set successfully"
        else:
            return "Frequency could not be set. Ensure that it is weekly or daily"

    def set_description(self,description:str):
        self.description = description
        return "Description set Successfully"

    def set_start_date(self, start_date:datetime):
        self.start_date= start_date

    def add_check(self, check_date):
        check_date = check_date.strftime("%Y-%m-%d")
        self.check_dates.append(check_date)
