#!/usr/bin/python3

class Parent:     #define parent class
    def myMethod(self):
        print('Calling parent method')

class Child(Parent): #defile child class
    def myMethod(self):
        print('Calling child method')

c=Child()        #instance of child
c.myMethod()     #child calls overridden method
