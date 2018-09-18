def divisors(k):
    my_list=[]
    for a in range(1,k):
        if k%a==0:
            my_list.append(a)
    return my_list
def find_integer_with_most_divisors(input_list):
    x=0
    integer=None
    for item in input_list:
        y=len(divisors(item))
        if y>x:
            x=y
            integer=item
    return integer
x=[8,12,18,6]
print(find_integer_with_most_divisors(x))
