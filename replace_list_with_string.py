def replace(my_list,string):
    new_list=my_list
    for n in range(1,4):
        new_list.pop(n)
        new_list.insert(n,string)
    return new_list
