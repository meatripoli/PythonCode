def find_gcd(some_list):
    gcd_list=[]
    m=len(some_list)
    gcd=[]
    for item in some_list:
        for n in range(1,item+1):
            if item%n==0:
                gcd_list.append(n)
    for item in gcd_list:
        if gcd_list.count(item)==m:
            gcd.append(item)
    x=gcd[0]
    for l in range(len(gcd)-1):
        if x<gcd[l]:
             x=gcd[l]
    return x
print(find_gcd([12,24,6,18]))
print(find_gcd([3, 5, 9, 11, 13]))
