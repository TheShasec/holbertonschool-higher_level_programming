#!/usr/bin/python3
""" 434 """


import csv
import json

def convert_csv_to_json(filename):
    """ 43 """
    try:
        with open(filename, "r") as mf:
            data = csv.DictReader(mf)
        with open(filename, "w") as mf:
            json.dump(list(data), "data.json")
        return True
    except Exception:
        return False
