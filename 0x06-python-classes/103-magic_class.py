#!/usr/bin/python3
# 103-magic_class.py
"""
Defines a class MagicClass
Created on Wed Dec 21 2022
@author: Iniovosa Michayah
"""
import math


class MagicClass:
    """The class for circle"""
    def __init__(self, radius=0):
        """The __init__ method for MagicClass class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculaes the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the perimeter of the circle"""
        return 2 * math.pi * self.__radius
