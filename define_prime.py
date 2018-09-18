def prime(n):
    is_number_prime=True
    for m in range(2,n):
        if n%m==0:
            is_number_prime=False
    if is_number_prime:
        return True
    else:
        return False
print(prime(7))
