#!/usr/bin/python3
# 5-to_json_string.py
# Iniovosa Michayah O
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
