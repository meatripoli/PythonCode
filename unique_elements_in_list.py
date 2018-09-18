def unique_elements(A):
    new_list=[]
    for item in A:
        if new_list.count(item)==0:
            new_list.append(item)
    return new_list
