def recursive_list_sum(data_list):
    total = 0
    for x in data_list:
        if type(x) == type([]):
            total = total + recursive_list_sum(x)
        else:
            total = total + x
    return total
# print (recursive_list_sum ([1, 2, [3,4]]))
