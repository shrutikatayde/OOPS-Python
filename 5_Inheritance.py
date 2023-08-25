# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 13:17:19 2023

@author: Lenovo
"""

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}.")
    
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python.")
        

#emp1 = Employee("Shruti", 20021)

emp1 = Programmer("shruu", 8888)
emp1.showLanguage()
emp1.showDetails()