# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:46:47 2023

@author: Lenovo
"""
class Employee:
    def __init__(self, name):
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"Thank you {self.name} !!"


e1= Employee("saru")
print(e1)

