#!/usr/bin/python3
""" 434 """


import csv
import json

def convert_csv_to_json(filename):
    """ 43 """
    try:
        with open(filename, "r") as mf:
            reader = csv.DictReader(mf)
            json.dump(list(reader), "data.json")
        return True
    except Exception:
        return False
