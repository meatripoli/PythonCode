def every_other_element(my_list):
    new_list=[]
    new_list.append(my_list[0])
    k=len(my_list)
    for a in range(1,k):
        if a%2==0:
            new_list.append(my_list[a])
    return new_list
