#!/usr/bin/python3
no =int(input('Enter any number: '))
numbers=[25,1,2,8,45,14,25,00,15,35,8]
for num in numbers:
    if num== no:
        print("Woho, we got the matching number..",no)
        break
else:
    print('Aha, you have to try again!')
