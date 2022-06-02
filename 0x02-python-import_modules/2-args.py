#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    if len(argv)-1 == 0:
        print("0 arguments.")
    elif len(argv)-1 == 1:
        print("1 argument:")
    else :
        print("{:d} arguments:".format(len(argv)-1))
    for arg in argv[1:]:
        print("{:d}: {:s}".format(i, arg))
        i = 1 + i
