#!/usr/bin/python3

for i in range(122, 96, -1):
    if i % 2 == 0:
        a = i
    else:
        a = i - 32
    print("{}".format(chr(a)), end="")
