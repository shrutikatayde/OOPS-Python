# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 19:06:22 2023

@author: Lenovo
"""

#Operator overloading

class Vector:
    def __init__(self, i, j, k):
        self.i= i
        self.j= j
        self.k= k
        
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    
    def __add__(self, x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
obj= Vector(3, 5, 7)
print(obj)
obj1= Vector(6, 8, 8)
print(obj1)
print(obj+obj1)
print(type(obj+obj1))


    
    
