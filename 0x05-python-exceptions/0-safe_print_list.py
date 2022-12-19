#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    indx = 0
    try:
        list1 = ""
        for elem in range(x):
            list1 += str(my_list[elem])
        print(list1[0:x])
        indx = x
    except IndexError:
        list1 = ""
        for i,elem in enumerate(my_list):
            list1 += str(elem)
        print(list1)
        indx = (i+1)
    return (indx)
