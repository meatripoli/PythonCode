def find_integer_with_most_divisors(input_list):
    my_list=[]
    count=0
    for item in input_list:
        for a in range(1,item+1):
            if item%a==0:
                count=count+1
        my_list.append(count)
        count=0
    x=my_list[0]
    for n in range(len(my_list)):
        if x<my_list[n]:
             x=my_list[n]
    my_index=my_list.index(x)
    return input_list[my_index]
x=[8,12,18,6]
print(find_integer_with_most_divisors(x))
