# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:07:36 2023

@author: Lenovo
"""

class Employee:
    companyName= "Apple"  #Class variable
    
    def __init__(self, name):  
        #instance variable
        self.name= name
        
    def showDetails(self):
        print(f"The name of employee is {self.name} and he is from Company {self.companyName}.")
        
emp1 = Employee("Shruti")
print(emp1.name)
emp1.companyName= "TCS"
emp1.showDetails()

emp2 = Employee("Saurav")
print(emp2.name)
emp2.showDetails()



 