import json
from datetime import datetime

class habit:
    def __init__(self,name:str, frequency:str, description:str, check_dates,start_date:datetime):
        """Create a habit 

        Inital point in creating new habits. 

        Args: 
            name: The name of the habit to be created 
            frequency: The defined frequency (Weekly/ or Monthly)
            description: A custom description of the habit 
            check_dates: The dates that the habit can already be checked. 
            start_date: The date that the habit was started
        """

        self.name = name.strip()
        self.set_frequency(frequency)
        self.description =  description
        self.check_dates =  check_dates
        self.start_date = start_date
    def __str__(self):
        """Return a string display of a habit
        """
        return f"Name: {self.name} \n\t- frequency: {self.frequency}\n\t- {self.description}\n\t- {self.start_date.strftime('%Y-%m-%d')}\n\t- {self.check_dates}\n"

    def as_dict(self):
        """Convert the habit object to a dict

        Hint: 
            1. This function is needed to convert the habit object for a fitting format to write to as json files. 
        """
        return {
            "name":self.name,
            "frequency":self.frequency,
            "description":self.description,
            "check_dates": self.check_dates,
            "start_date":self.start_date.strftime("%Y-%m-%d")
        }
    def set_name(self,name:str):
        """ Set the Name of the Habit

        Hint: 
            1. This function will change the habit name and return a string message if successful. 
        """
        self.name = name
        return "Name set successfully"

    def set_frequency(self,frequency:str):
        """ Set the frequency of the habit

        Hint: 
            1. This function will check if the habit is daily or weekly 
            2. This function will change the habit name and return a string message if successful. 
        """
        if frequency == "weekly" or frequency == "daily":
            self.frequency = frequency
            return "Frequency set successfully"
        else:
            return "Frequency could not be set. Ensure that it is weekly or daily"

    def set_description(self,description:str):
        """ Set the description of the habit

        Hint: 
            1. This function will change the habit name and return a string message if successful. 
        """
        self.description = description
        return "Description set Successfully"

    def set_start_date(self, start_date:datetime):
        """ Set the start_date of the habit

        Hint: 
            1. This function will change the habit name and return a string message if successful. 
        """
        self.start_date= start_date
        return "start_date set Successfully"

    def add_check(self, check_date:datetime):
        """ Add a check to the list of checked dates

        Hint: 
            1. This function will change the habit name and return a string message if successful. 
            2. This functionwill check if the date is already in the list of checked habits. 
        """

        check_date = check_date.strftime("%Y-%m-%d")
        if check_date in self.check_dates:
            return f"{check_date} is already checked."
        self.check_dates.append(check_date)
        return f"{check_date} successfully check"

    def delete_check(self,  delete_date):
        """ This function will delete a check date from the list of check dates"""
        delete_date = delete_date.strftime("%Y-%m-%d")
        self.check_dates.remove(delete_date)
        return f"{delete_date} sucessfully removed from check"

    def longest_streak(self):
        """ This function will get a the longest streak for the habits

        Hint: 
            1. It works by checking if the frequency is set to daily and if it is we define the delta to be 1 day otherwise it will be 7. 
            2. The delta will be used to check if any check occurs within the next delta so for a week the check can be on any day in the next 7 days in order to count as valid streak
        """


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

        return f"{self.name} has the frequency {self.frequency} and its longest streak is {longest_streak}"
