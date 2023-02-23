import pandas as pd
import asyncio
import time 
import json
from unittest.mock import AsyncMock
import subprocess

class Backend:
    def __init__(self, json_filepath) -> None:
        self.data = 0
        self.event_list = []
        self.event_date_list = []
        self.json_filepath = json_filepath
        self.read_json(self.json_filepath)
        self.get_events_dates()
        pass

    def read_json(self, filename):
        try:
            with open(filename, "r") as json_file:
                self.data = json.load(json_file)
                print(self.data)
        except FileNotFoundError:
            print("Test list file not found. Please check the file path and try again.")
        except json.JSONDecodeError:
            print("Error decoding JSON data in test list file. Please check the file format and try again.")
    
    def get_events_dates(self):
        for key, value in self.data.items():
            self.event_list.append(key)