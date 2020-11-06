#keyword Argument
#This allows you to skip arguments or place them out of order because the Python
#interpreter is able to use the keywords provided to match the values with parameters. You
#can also make keyword calls to the printme() function in the following ways-
#Order of the parameters does not matter

#!/usr/bin/python3
#Function definition is here
def printinfo(name,age):
    print("Name: ",name)
    print("Age: ", age)
    return
age=int(input("Please enter the age: "))
if (age>60):
    print("You are 60+")

name=input("Please enter the name: ")
print("***Nice Name****")
print("\n What I got from you is:\n")
printinfo(name, age)
print("Would you like to edit or save?")
print("Type 1 for Edit or 2 for Save")
res=int(input())
while (res==1):
#if res==1:
    age = int(input("Please enter the age: "))
    if (age > 60):
        print("You are 60+")

    name = input("Please enter the name: ")
    print("***Nice Name****")
    print("\n What I got from you is:\n")
    printinfo(name, age)
    print("Would you like to edit or save?")
    print("Type 1 for Edit or 2 for Save")
    res = int(input())
#elif res==2:
if res==2:
    print("We have saved your details. Thank you.")
    print("***Good bye***")
else:
    print("\n you have not selected the right choice. Good Bye.\n")