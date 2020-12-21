#!/usr/bin/python
try:
    fh=open("testfile1","w")
    fh.write("I am writing in the file line 1")
finally:
    print("I am being print from finally block")
    fh.close()
