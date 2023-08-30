# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:32:28 2023

@author: Lenovo
"""

#Single ineritance

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Sound of animal")
        
class dog(Animal):

    def make_sound(self):
        print("Barking..")
        
dogi = dog("chiku", "whiteDog")
print(dogi.name)
print(dogi.species)
dogi.make_sound()


anim = Animal("petu", "blackdog")
print(anim.name)
print(anim.species)
anim.make_sound()


