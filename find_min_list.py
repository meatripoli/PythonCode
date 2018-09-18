def what_is_the_min(list):
    n=0
    x=list[0]
    for n in range(len(list)):
        if x>list[n]:
             x=list[n]
    return x
