#!/usr/bin/python3
import sys
i = 1
if len(sys.argv)-1 == 0:
    print("0 arguments.")
elif len(sys.argv)-1 == 1:
    print("1 argument:")
else :
    print("{} arguments:".format(len(sys.argv)-1))
for arg in sys.argv[1:]:
    print("{}: {}".format(i, str(sys.argv[i])))
    i = 1 + i
