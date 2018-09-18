def divisors(k):
    my_list=[]
    for a in range(1,k+1):
        if k%a==0:
            my_list.append(a)
    return my_list
x=8
print(divisors(x))
