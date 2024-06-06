import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
datafolder = os.path.join(BASE_DIR, "data")
datasource = os.path.join(datafolder, "users.json")

def check_dataset_exists():
    if not os.path.exists(datafolder):
        os.mkdir(datafolder)
    if not os.path.exists(datasource):
        with open(datasource, "w") as f:
            json.dump({"data": []}, f)  # Initialize the file with an empty data array

def read_usersdata():
    check_dataset_exists()
    with open(datasource, "r") as f:
        users = json.load(f)
    return users

def add_userdata(user: dict):
    users = read_usersdata()
    with open(datasource, "w") as f:
        users["data"].append(user)
        json.dump(users, f, indent=2)

