#!/usr/bin/python3

def weight_average(my_list=[]):
    mul_list = [x[0] * x[1] for x in my_list]
    freq_list = [x[1] for x in my_list]
    sum_list = sum(mul_list)
    if sum(freq_list) == 0:
        return 0
    return sum_list / sum(freq_list)
