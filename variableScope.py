#!/usr/bin/python3
total = 0 # This is global variable.

#Function definition is here
def sum(arg1, arg2):
    #Add both the parameters and return them.
    total = arg1+arg2;  # Here total is local variable
    print("Inside the function local total:", total)
    return total

#Now you can call sum function
sum(10,30)
print("Outside the function global total",total)


#Output:
#Inside the function local total: 40
#Outside the function global total 0