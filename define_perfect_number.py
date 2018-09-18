def perfect_number(n):
    summ=0
    for number in range(1,n):
        if n%number==0:
            summ=summ+number
    if summ==n:
        return True
    else:
        return False
