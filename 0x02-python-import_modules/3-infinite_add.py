#!/usr/bin/python3

from sys import argv

sum = 0
for arg in argv[1:]:
    sum += int(arg)

print(sum)
