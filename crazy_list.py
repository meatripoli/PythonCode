def crazy_list(some_list):
    y=len(some_list)
    new_list=[]
    for n in range(0,y):
        new_list.append(some_list[(y-1)-n])
    if some_list==new_list:
        return True
    else:
        return False
x=[5, 6, 8, 9, 'PYTHON', 9, 8, 6, 5]
print(crazy_list(x))
y=[4, 5, 6, 7, 8, 4, 5, 2]
print(crazy_list(y))
