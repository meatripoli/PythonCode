def remove_first_and_last(A):
    new_list=A
    new_list.remove(new_list[0])
    new_list.remove(new_list[-1])
    #or
    #newlist = input_list[1:-1]
    return new_list
    
