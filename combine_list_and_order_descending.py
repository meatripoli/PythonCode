def combine_and_order(A,B):
    count=0
    A_plus_B=A+B
    for items in A_plus_B:
        count=count+1
    unSorted = True
    while unSorted:
        unSorted = False
        for n in range(0,count-1):
            if A_plus_B[n]<A_plus_B[n+1]:
                temporary_variable = A_plus_B[n]
                A_plus_B[n] = A_plus_B[n + 1]
                A_plus_B[n + 1] = temporary_variable
                unSorted = True
    return A_plus_B
