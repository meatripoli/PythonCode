def magnitude(vector):
    add=0
    for n in range(0,len(vector)):
        add=add+vector[n]**2
    x=add**(1/2)
    return x
def normalize(vector):
    norm=list(range(0,len(vector)))
    for n in range(0,len(vector)):
        norm[n]=vector[n]/magnitude(vector)
    return norm
x=[2,3,-4]
print(normalize(x))
