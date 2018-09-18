def ascending_order(my_list):
    count=0
    y=len(my_list)
    unSorted = True
    while unSorted:
        unSorted = False
        for n in range(0,y-1):
            if my_list[n]>my_list[n+1]:
                temporary_variable = my_list[n]
                my_list[n] = my_list[n + 1]
                my_list[n + 1] = temporary_variable
                unSorted = True
    return my_list
