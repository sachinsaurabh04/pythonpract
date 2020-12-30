#!/usr/bin/python3
class Parent:  # define parent class
    parentAttr = 100
    def __init__(self):
        print("calling parent constructor")
    def parentMethod(self):
        print('calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("parent attribute:", Parent.parentAttr)

class Child(Parent):    #define child class
    def __init__(self):
        print("calling child constructor")

    def childMethod(self):
        print('calling child method')

c=Child()    #instance of child
c.childMethod()   #child calls its method
c.parentMethod()   #calls parent's method
c.setAttr(200)    #again call parent's method
c.getAttr()    #again call parent;s method





"""
O/p:
calling child constructor
calling child method
calling parent method
parent attribute: 200
"""