def _list_of_primes_sample_(n):
    my_list = []
    integer = 2
    while integer < n:
        prime = True
        start = 2
        while start < integer:
            if integer % start == 0:
                prime = False
            start = start + 1
        if prime == True:
            my_list.append(integer)
        integer = integer + 1
    return my_list
