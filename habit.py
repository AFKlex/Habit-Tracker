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
