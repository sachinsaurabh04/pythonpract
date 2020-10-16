d= (input("Enter the number to compare: "))

if d.isdigit():
    a=int(d)
    if(a==30):
        print(" Your Input is equal to 30")
    elif(a<30):
        print(" Your Input smaller than 30")
    elif(a>30):
        print(" Your Input greater than 30")
else:
    if d.isupper():
        print("\n")
        print("***I don't know how to compare a string with the number... Do you know, how to? ***")
        print("***you have entered the text in CAPITAL character***")
    else:
        print(" ****I don't know how to compare a string with the number... Do you know, how to?*** ")
        print("***you have entered the letters in LOWER or MiXeD*** ")

