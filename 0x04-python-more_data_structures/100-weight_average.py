#!/usr/bin/python3
def weight_average(my_list=[]):
    mul_list = [x[0] * x[1] for x in my_list]
    frequent_list = [x[1] for x in my_list]
    sumed_list = sum(mul_list)
    if sum(frequent_list) == 0:
        return 0
    return sumed_list / sum(frequent_list)
