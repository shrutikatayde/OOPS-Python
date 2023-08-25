# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:40:05 2023

@author: Lenovo
"""
#decorator for GETTER AND SETTER

class MyClass:
    def __init__(self, value):
        self._value = value
        
    def show(self):
        print(f"Value is {self._value}")
    
    @property  #getter
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value= new_value/10
        
obj= MyClass(10)
obj.ten_value=67
print(obj.ten_value)
obj.show()
     

        
                      
    
    
    