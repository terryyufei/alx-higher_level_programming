#!/usr/bin/python3

from sys import argv

add = 0
for arg in argv[1:]:
    add += int(arg)

print(add)
