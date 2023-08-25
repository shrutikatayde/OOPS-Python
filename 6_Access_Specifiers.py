# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 01:27:18 2023

@author: Lenovo
"""
#ACCESS SPECIFIERS
#1. Public
#2. Private
#3. Protected

'''class Employee:
    def __init__(self):
        self.__name="shruti"  #private variable denote by double underscore but it in weak indivator as it it access by "_class__attribute" name before it called as NAME MANGLING
        self._id= 1234  #Public variable as single underscore at starting is nothiing but normal variable declaration
        
a= Employee()
#print(a.__name) #Cannot be accesses directly
print(a._Employee__name) #can be accessed indirectly  #private attribute
print(a._id) #can be access directly as it is '''  



class Student:
    def __init__(self):
        self._name= "Shruti" 
        
    def _funName(self):   #Protected method
        return "Python learning"
    
class Subject(Student):  #inheritated class
    pass

obj1= Student()
obj2 = Subject()

print(obj1._name)
print(obj1._funName())


print(obj2._name)
print(obj2._funName())
    
        
