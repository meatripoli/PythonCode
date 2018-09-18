def modify_list(A):
    x=len(A)
    for n in range(0,x):
        if A[n]%2!=0:
            temp_value=A.pop(n)
            A.insert(n,(temp_value+1))
    return A
