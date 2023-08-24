# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 08:25:38 2023

@author: Lenovo
"""

class Person:
    def __init__(self, n, o):  # Constructor
        self.name= n
        self.occ = o
    
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=Person("Shruti", "Full-Stack Developer")
b=Person("Saurabh", "Software Developer")
a.info()
b.info()