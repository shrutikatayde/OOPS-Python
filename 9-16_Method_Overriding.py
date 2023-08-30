# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 21:18:15 2023

@author: Lenovo
"""

#METHOD OVERRIDING

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y= y
        
    def area(self):
        return self.x*self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self):
        return 3.14*super().area()
    
obj = Circle(3)
print(obj.area())
        