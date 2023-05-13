#!/usr/bin/python3
if __name__ == '__main__':
    from hidden_4 import *
    d = dir
    for i in range(0, len(d)):
        if d[i][0:2] != "__":
            print("{}".format(d[i]))
