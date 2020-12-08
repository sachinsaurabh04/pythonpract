#!/usr/bin/python3
# Open a file
fo = open("foo.txt", "r+")
fo.write( "Python is a great language.\nYeah its great!!\n")
#Open a file
str = fo.read() #It will let the str print full text file
#str = fo.read(10)   #It will print only 10 letter of the file
print(str)
position = fo.tell()
print("Current file position : ", position)
#reposotion pointer at the beginning once again
position= fo.seek(0,0)
str = fo.read(10)
print("Again read String is : ", str)
# Close opend file
fo.close()