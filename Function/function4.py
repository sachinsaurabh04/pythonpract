#!/usr/bin/python3
#This is an example where argument is being passed by reference and the reference is being overwritten inside the called function.
def changeme(mylist):
    mylist = [1,2,3,4]
    print("the actual value of the list is: ", mylist)
    return()
mylist = [10,20,30]
changeme(mylist)
print("Printing the mylist",mylist)
mylist[2]=33
print("printing mylist from outside",mylist)
changeme(mylist)
