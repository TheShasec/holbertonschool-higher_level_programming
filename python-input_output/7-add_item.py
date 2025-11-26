#!/usr/bin/python3
"""4324"""


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
import sys

args = sys.argv
ml = load_from_json_file("add_item.json")
if len(args) > 1:
    for arg in args[1:]:
        ml.append(arg)
    save_to_json_file(ml, "add_item.json")
else:
    save_to_json_file(ml, "add_item.json")
