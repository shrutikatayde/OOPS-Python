# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 13:44:21 2023

@author: Lenovo
"""
#for method
class ParentClass:
    def parent_method(self):
        print("This is the parent method")
    
class ChildClass(ParentClass):
    def parent_method(self):
        print("This is the child parent method")
    def child_method(Self):
        print("This is the child method")
        super().parent_method()


child_obj= ChildClass()
child_obj.child_method()
child_obj.parent_method()


#for variable

class Employee:
    def __init__(self, name, id):
        self.name= name
        self.id = id
        
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
        
shruti = Employee("Shruti Tayde", 1234)
saurabh= Programmer("Saurabh Tayde", 5678, "C++")

print(shruti.name)
print(saurabh.name)
print(saurabh.lang)       