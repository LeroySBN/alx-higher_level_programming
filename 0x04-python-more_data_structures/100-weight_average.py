#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list in []:
        return 0
    total, wgh = 0, 0
    for i in range(len(my_list)):
        wgh += my_list[i][0] * my_list[i][1]
        total += my_list[i][1]
    return (wgh/total)
