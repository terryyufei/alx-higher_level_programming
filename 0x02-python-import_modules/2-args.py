#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    n = len(argv) - 1
    if n == 0:
        print("{} arguments.". format(n))
    elif n == 1:
        print("{} argument:".format(n))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(n))
        i = 1
        for arg in argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1
