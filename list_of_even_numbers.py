def list_of_all_even_numbers(a,b):
    my_list=[]
    for k in range(a,b):
        if k%2==0:
            my_list.append(k)
    return my_list
