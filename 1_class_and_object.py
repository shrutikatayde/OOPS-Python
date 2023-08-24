# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 08:25:39 2023

@author: Lenovo
"""

#OOPS Concept


class Person:
    name="Shruti"
    occupation= "Student"
    networth= 10
    
    def info(self): # self means call those object for which method is called
        print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()

print(a.name, a.occupation)

a.name= "Saurav"
a.occupation="Software developer"

b.name = "Nikita"
b.occupation = "HR"


print(a.name, a.occupation)
print(b.name, b.occupation)

a.info()
b.info()