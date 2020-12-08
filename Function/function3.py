#!/usr/bin/python3
# Pass by reference vs value
# Function definition is here
def changeme(mylist):
    "This changes a passed list into this function"
    print ("values inside the function before change: ", mylist)
    mylist[2]=50
    print("Values inside the function after change:", mylist)
    mylist[3]=99
    print("value after chaning 99 in the list is ",mylist)
    mylist.append(432)
    print("after APPENDING the value is ",mylist)
    #return
#Now you can call changeme function
mylist = [10,20,30,70,22]
changeme(mylist)
print("Values OUTSIDE the function:", mylist)
