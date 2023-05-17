#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    number_list = list(my_set)
    result = sum(my_set)
    return result
