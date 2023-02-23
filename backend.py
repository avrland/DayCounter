import pandas as pd
import asyncio
import time 
import json
from unittest.mock import AsyncMock
import subprocess

class Backend:
    def __init__(self, json_filepath) -> None:
        self.data = 0
        self.json_filepath = json_filepath
        self.read_json(self.json_filepath)
        self.event_list = self.get_events()
        pass

    def read_json(self, filename):
        try:
            with open(filename, "r") as json_file:
                self.data = json.load(json_file)
                print(self.data)
                return 0
        except FileNotFoundError:
            return "Test list file not found. Please check the file path and try again."
        except json.JSONDecodeError:
            return "Error decoding JSON data in test list file. Please check the file format and try again."
    
    def get_events(self):
        events_list = []
        for key, value in self.data.items():
            events_list.append(key)
        return events_list