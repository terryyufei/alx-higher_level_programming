#!/usr/bin/python3

for i in range(10):
    for j in range(i+1, 10):
        if i != 0:
            print("{:d}{:d}, ".format(i, j), end="")
        else:
            print("{:02d}, ".format(j), end="")
print()
