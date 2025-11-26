#!/usr/bin/python3
"""4324"""


import save_to_json_file from "5-save_to_json_file"
import load_from_json_file from "6-load_from_json_file"
import sys

args = sys.argv
ml = []
if len(args) > 1:
    for arg in args[1:]:
        ml.append(arg)
    save_to_json_file(ml, "add_item.json")
else:
    save_to_json_file(ml, "add_item.json")
