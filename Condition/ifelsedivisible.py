#num1=int(input("Enter the number you want to check: "))
#if (num1%2==0):
#    print("Number is even number")
#else:
#    print("Number is odd.")

numb=input("Enter the number:")
if numb.isdigit():
    if int(numb)%2==0:
        if int(numb)%3==0:
            print("Number is divisible by 2 & 3 both.")
        else:
            print("Number is divisible by 2 only")

    elif int(numb)%3==0:
        print("Number is divisible by 3 only.")

    else:
        print("Number is not divisible by 2 or 3")
else:
    print("Enter a valid number between 0-9.")