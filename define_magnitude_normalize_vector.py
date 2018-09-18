def normalize(vector):
    norm=list(range(0,len(vector)))
    for n in range(0,len(vector)):
        norm[n]=vector[n]/magnitude(vector)
    return norm
def magnitude(my_vector):
    add=0
    for n in range(0,len(my_vector)):
        add=add+my_vector[n]**2
    x=add**(1/2)
    return x
