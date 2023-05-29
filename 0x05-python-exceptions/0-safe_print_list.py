#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            n += 1
    except IndexError:
        pass
    finally:
        print()
        return n
