import json
import os


def load_data(file_name: str) -> json:
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
    else:
        return {}
