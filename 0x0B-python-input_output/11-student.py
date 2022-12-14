#!/usr/bin/python3
# 11-student.py
# Iniovosa Michayah O
"""
a class Student
"""


class Student:
    """
    Definition of the Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of the class with:
        first_name
        last_name
        age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
        of a Student instance:
            If attrs is a list of strings, only attribute names
            contained in this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """
        if type(attrs) == list:
            if all(type(elem) == str for elem in attrs):
                return {key: getattr(self, key)
                        for key in attrs if hasattr(self, key)}
        class_dict = self.__dict__
        return class_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance:
            You can assume json will always be a dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
