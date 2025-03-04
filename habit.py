import json
from datetime import datetime
class habit:
    def __init__(self,name, frequency, description, checkDates,startDate:datetime):
        self.name = name.strip()
        self.frequency = frequency
        self.description =  description
        self.checkDates =  checkDates
        self.startDate = startDate
    def __str__(self):
        return f"Name: {self.name} \n\t- frequency: {self.frequency}\n\t- {self.description}\n\t- {self.startDate}\n\t- {self.checkDates}\n"

    def asDict(self):
        return {
            "name":self.name,
            "frequency":self.frequency,
            "description":self.description,
            "checkDates":self.checkDates,
            "startDate":self.startDate.strftime("%Y-%m-%d")
        }
    def setName(self,name:str):
        self.name = name
        return "Name set successfully"

    def setFrequency(self,frequency:str):
        if frequency == "weekly" or frequency == "daily":
            self.Frequency = frequency
            return "Frequency set Successfully"
        else:
            return "Frequency could not be set. Ensure that it is weekly or daily"

    def setDescription(self,description:str):
        self.description = description
        return "Description set Successfully"

    def setStartDate(self, startDate:datetime):
        self.startDate= startDate

