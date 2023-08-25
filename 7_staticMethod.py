# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:46:19 2023

@author: Lenovo
"""
#static method

def add(a, b):
    return a+b

class Math:
    def __init__(self, num):
        self.num= num
    
    def addToNum(self, n):
        self.num= self.num + n
        
    @staticmethod
    def add(a, b):
        return a+b
    
a=Math(5)
print(a.num)
a.addToNum(6)
print(a.num)
print(add(7, 3))  #Math. , a.