num = input("Enter your number ")

print("\n")
if num.isdigit():
    print("You have entered:",num, "\n It's a Number.")
else:
    print("You have entered:",num, "\n It's a String or Mixed.")
    print("Please enter the numbers only.")