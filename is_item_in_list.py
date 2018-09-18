def is_item_in_list(my_list,item):
    count=0
    element=0
    for items in my_list:
        count=count+1
    for n in range(0,count-1):
        if item==my_list[n]:
            element=element+1
    return element
