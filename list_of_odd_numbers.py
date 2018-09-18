def list_of_all_odd_numbers(a,b):
    my_list=[]
    for k in range(a,b+1):
        if k%2!=0:
            my_list.append(k)
    my_list.reverse()
    return my_list
