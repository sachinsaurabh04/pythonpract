#!/usr/bin/python3
#Function Argument
    #. Required arguments
    #. Keyword arguments
    #. Default arguments
    #. variable-length arguments

#Required Arguments
#To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error
#function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return
#now you can call printme function
printme("hello")