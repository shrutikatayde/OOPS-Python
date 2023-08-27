# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:27:33 2023

@author: Lenovo
"""

class Library:
    def __init__(self):
        self.noBooks= 0
        self.books = {}
        
    def addBook(self,t):
        for i in range(0, t):
            newBook, author= input("Enter the name of book: ").split()
            self.books[newBook]= author
        self.noBooks = len(self.books)
        
    def showInfo(self):
        print(f"\nThe Library has {self.noBooks} books. The books are :\n\n Book Name \t\t Author Name\n ----------------------------- ")
        for book in self.books:
            print(" ",book,"|\t", self.books[book])
        
l1 = Library()
t=int(input("How many you want to add at a time: "))

l1.addBook(t)
l1.showInfo()
    