def pattern_sum(a, b):
    previous_value=0
    my_list=[]
    for n in range(b):
        number=((10**n)*a)+previous_value
        my_list.append(number)
        previous_value=number
    total=sum(my_list)
    return total
print(pattern_sum(5,3))
print(pattern_sum(4,5))

##proff's way
#def _chain_of_number_sample_ed2_(a, b):
#    chain_list = []
#    my_sum = 0
#    for x in range(1, b+1):
#        chain_list.append(x*str(a))
#    for items in chain_list:
#        my_sum = my_sum + int(items)
#
#    return my_sum
