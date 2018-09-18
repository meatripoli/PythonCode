def items_price(a, b):
    total=0
    number_of_items=len(a)
    for n in range(0,number_of_items):
        total+=(a[n]*b[n])
    return total
a = [2, 3, 5, 7, 9]
b = [5, 8, 4, 1, 11]
print(items_price(a,b))
