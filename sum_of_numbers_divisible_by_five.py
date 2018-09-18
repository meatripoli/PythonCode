iteration=1
number=1
summ=0
while number<=101:
    if number%5==0:
        summ=summ+number
        print('Iteration: ',iteration,'The sum is: ',summ)
        iteration=iteration+1
    number=number+1
print('The sum of all numbers between 1 and 101 that are divisible by 5 is: ',summ)
