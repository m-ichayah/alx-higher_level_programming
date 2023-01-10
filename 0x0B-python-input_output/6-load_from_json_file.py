#!/usr/bin/python3
# 5-to_json_string.py
# Iniovosa Michayah O

"""
a function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    JSON representation creating an object
    from JSON file
    """
    with open(filename) as f:
        obj_create = json.load(f)
        return 
