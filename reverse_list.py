def reverse_list(A):
    y=len(A)
    new_list=[]
    for n in range(0,y):
        new_list.append(A[(y-1)-n])
    return new_list
