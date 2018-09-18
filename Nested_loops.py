#Nested while loops
number=2
end_number=50
while number<=end_number:
    prime=True
    divisor=2
    while number>divisor:
        if number%divisor==0:
            print(number,' is not prime')
            prime=False
            break
        divisor=divisor+1
    if prime:
        print(number,' is prime')
    number=number+1
#Nested for loops
number=2
end_number=50
for current_number in range(number,end_number+1):
    prime=True
    for divisor in range(2,current_number):
            if current_number%divisor==0:
                prime=False
                break
    if prime:
        print(current_number,' is a prime')
