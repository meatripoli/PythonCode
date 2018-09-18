m=int(input('Enter a positive integer:'))
n=1
spaces=0
dummy=m-1
while n<=m:
    star='*'
    if n==m:
        x=star
    else:
        x=(dummy*star)+(spaces*' ')+(star)
    print(x)
    dummy=1
    spaces=(m-3)-(n-1)
    n=n+1
