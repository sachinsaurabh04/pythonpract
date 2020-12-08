#keyword Argument
#This allows you to skip arguments or place them out of order because the Python
#interpreter is able to use the keywords provided to match the values with parameters. You
#can also make keyword calls to the printme() function in the following ways-
#Order of the parameters does not matter

#!/usr/bin/python3
#Function definition is here
def printinfo(name,age):
    print("NAME: ",name)
    print("AGE: ", age)
    return

def calculation():
    age=int(input("Please enter the age: "))
    if (age>60):
        print("You are 60+")
    name=input("Please enter the name: ")
    print("***Nice Name****")
    print("\nWhat I got from you is: ")
    printinfo(name, age)
    return()

calculation()
print("\nWould you like to edit or save? Press 1 for Edit or 2 for Save: ")
res = int(input())

while (res==1):
    calculation()
    print("\nWould you like to edit or save? Press 1 for Edit or 2 for Save: ")
    res = int(input())

if res==2:
    print("\nWe have SAVED your details. Thank you.")
    print("***Good bye***")

else:
    print("you have not selected the right choice. Good Bye.")