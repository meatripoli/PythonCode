mylist=[i for i in range(1001)]
summ=0
i=1
while i<=1001:
    summ=summ+mylist[i]
    print('Iteration: ',i,' Sum: ',summ,'number: ',mylist[i])
    i=i+3
print('The sum is: ',summ)
