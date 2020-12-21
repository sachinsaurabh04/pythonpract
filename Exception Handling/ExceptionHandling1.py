#!/usr/bin/python
#This example opens a file, writes content in the file and comes out gracefully because there is no problem at all.
try:
    fh=open("testfile","w")
    fh.write("This is my test file for exception handling")
except IOError:
    print("Error: can't find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()
