import pandas as pd
from datetime import datetime
import asyncio
import time 
import os
import json
from unittest.mock import AsyncMock
import subprocess

class Backend:
    def __init__(self) -> None:
        self.data = {}
        self.event_list = []
        self.event_date_list = []
        self.read_json()
        self.get_events_list()
        pass

    def read_json(self):
        try:
            # Find the first JSON file in the current directory
            for filename in os.listdir('.'):
                if filename.endswith('.json'):
                    with open(filename, "r") as json_file:
                        self.data = json.load(json_file)
                        print(self.data)
                        return  # exit the loop after reading the first JSON file
            # If no JSON file was found, raise a FileNotFoundError
            raise FileNotFoundError
        except FileNotFoundError:
            print("No JSON file found in the current directory. Please check the file path and try again.")
        except json.JSONDecodeError:
            print("Error decoding JSON data in test list file. Please check the file format and try again.")
    
    def get_events_list(self):
        self.event_list = []
        for key, value in self.data.items():
            self.event_list.append(key)

    def return_events_list(self):
        return self.event_list
    
    def get_event_date(self, key):
        event_date = self.data.get(key,"Error")
        return event_date
    
    def get_days_from_event(self, key):
        given_date_str = self.data.get(key)
        days_since_event = self.get_days_from_date(given_date_str)
        return days_since_event
    
    def get_days_from_date(self, date):
        given_date = datetime.strptime(date, "%d.%m.%Y")
        current_date = datetime.now()
        days_since_event = (current_date - given_date).days
        return days_since_event