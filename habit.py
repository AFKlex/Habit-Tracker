import json
from datetime import datetime
import timedelta
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
        if check_date in self.check_dates:
            return f"{check_date} is already checked."
        self.check_dates.append(check_date)
        return f"{check_date} successfully check"

    def delete_check(self,  delete_date):
        delete_date = delete_date.strftime("%Y-%m-%d")
        self.check_dates.remove(delete_date)
        return f"{delete_date} sucessfully removed from check"

    def longest_streak(self):
        dates = [datetime.strptime(date,"%Y-%m-%d")for date in self.check_dates] #Convert to Dates
        dates = sorted(dates) # Sort Dates 
        longest_streak =0
        current_streak =1

        if self.frequency == "daily":
            timedelta = 1 # Daily Delta
        else:
            timedelta = 7 # Weekly Delta 

        for i in range(len(dates)-1): # Loop all Dates
            current_date = dates[i]
            next_date = dates[i+1]

            if (next_date - current_date).days <= timedelta: # Check if the timedelta is within the valid delta
                current_streak +=1
                #print(f"{current_date.strftime('%Y-%m-%d')} is followed by {next_date.strftime('%Y-%m-%d')}")
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak =1

        if current_streak > longest_streak:
            longest_streak = current_streak

        return f"Habit {self.name} has the frequency {self.frequency} and its longest streak is {longest_streak}"
