# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:28:03 2023

@author: Lenovo
"""

#Decoretors ---> use for modifing the flow/behavior of 
#                function and adding more functionalities.


def greett(fun):
    def mfx(*args, **kargs):
        print("Good Morning!!")
        fun(*args, **kargs)
        print(f"Thanks for using {fun.__name__}() function")
    return mfx

@greett
def hello():
    print("Hello World")  

@greett      
def add(a, b):
    print(a+b)

hello()
add(1, 2)
        