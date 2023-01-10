#!/usr/bin/python3
# 5-to_json_string.py
# Iniovosa Michayah O

"""
a function that returns an object
(Python data structure) represented
by a JSON string
"""


import json


def from_json_string(my_str):
    """
    JSON representation of an object
    """
    load_json = json.loads(my_str)
    return load_json
