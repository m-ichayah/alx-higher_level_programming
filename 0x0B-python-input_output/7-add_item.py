#!/usr/bin/python3
# 7-add_item.py
# Iniovosa Michayah O
"""
a script that adds all arguments
to a Python list, and then save
them to a file
"""


import sys

if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    try:
        list_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        list_items = []
    list_items.extend(sys.argv[1:])
    save_to_json_file(list_items, "add_item.json")