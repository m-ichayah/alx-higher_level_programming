#!/usr/bin/python3
# 8-class_to_json.py
# Iniovosa Michayah O

"""
a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    A class to JSON object
    """
    obj_dict = obj.__dict__
    return obj_dict
