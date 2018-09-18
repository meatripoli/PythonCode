def list_of_primes(n):
    my_list=list(range(2,n))
    for m in range(2,n):
        if n%m==0:
            my_list.remove(m)
    return my_list
n=14
print(list_of_primes(n))
