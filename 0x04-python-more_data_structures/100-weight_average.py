#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_sum = []
    total_weight = 0

    for score, weight in my_list:
        total_sum.append(score * weight)
        total_weight += weight
    weight_average = sum(total_sum) / total_weight
    return weight_average
