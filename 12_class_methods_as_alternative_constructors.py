# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 14:53:54 2023

@author: Lenovo
"""

#class methods as alternative constructor

class Employee :
    def __init__(self, name, salary):
        self.name= name
        self.salary = salary
        
    @classmethod 
    def fromStr(cls, string ):
        return cls(string.split("-")[0], int(string.split("-")[1]))
    
e1 = Employee("Shrutika", 120000)
print(e1.name)
print(e1.salary)

string= "Saurabh tayde - 250000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary+10000)