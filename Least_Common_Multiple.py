def least_common_multiple(a,b):
    m=a
    while m%b!=0:
        m=m+a
    return m
