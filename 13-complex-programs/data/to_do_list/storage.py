import os

from dataclasses import asdict
import json

from models import Task

def load(filename):

    if not os.path.exists(filename):
        return []

    with open(filename, "r", encoding="utf-8") as f:

        data = json.load(f)

    return [
        Task(**item)
        for item in data
    ]
def save(filename,tasks):
    data=[
        asdict(task)
        for task in tasks
    ]
    temp_file = filename + ".tmp"

    with open(temp_file, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=2
        )

    os.replace(temp_file, filename)