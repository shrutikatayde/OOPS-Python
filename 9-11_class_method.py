# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 12:57:31 2023

@author: Lenovo
"""

class Employee:
    company= "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
        
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany
        
e1 = Employee()
e1.name  = "Shruta"
e1.show()
e1.changeCompany("tesla")
print(Employee.company)
e1.show()
print(Employee.company)

    
    