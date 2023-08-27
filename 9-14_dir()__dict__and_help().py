# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:05:32 2023

@author: Lenovo
"""

#some helfpul methods ===>> dir(), __dict__, help() 

class Person:
    def __init__(self, name, salary):
        self.name= name
        self.salary=salary
        
p= Person("Shrutika", 1000000)
print(dir(p))
print(p.__dict__)
print(help(Person))
        