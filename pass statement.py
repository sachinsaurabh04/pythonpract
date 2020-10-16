#========pass statement==========
#It is used when a statement is required syntactically but you do not want any command
#or code to execute.
#The pass statement is a null operation; nothing happens when it executes. The
#pass statement is also useful in places where your code will eventually go, but has not
#been written yet i.e. in stubs).

#!/usr/bin/python3
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is pass block')
    print('Current letter : ', letter)
print('Good Bye')