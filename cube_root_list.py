def cube_root_list(k):
    my_list=[]
    if k==1:
        return my_list
    else:
        for a in range(1,k):
            my_list.append(a**(1/3))
    return my_list
