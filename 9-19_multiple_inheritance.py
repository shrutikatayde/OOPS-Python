# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 09:12:21 2023

@author: Lenovo
"""
# Multiple inheritance


class Dance:
    def __init__(self, typeOfDance):
        self.typeOfDance = typeOfDance


class Dancer:
    def __init__(self, name):
        self.name = name


class DancerName(Dance, Dancer):
    def __init__(self, typeOfDance, name):
        self.typeOfDance = typeOfDance
        self.name = name


obj = DancerName("Kathak", "Shruti")
print(obj.name)
print(obj.typeOfDance)
print(DancerName.mro())
