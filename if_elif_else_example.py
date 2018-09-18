user_response=input('What is the temperature outside in Celsius? ')
Celsius=float(user_response)
Fahrenheit=((Celsius*9)/5)+32
print('The Temperature in Fajrenheit is: ',Fahrenheit,'F')
if Fahrenheit<32:
    print('It is freezing')
elif Fahrenheit<50:
    print('It is chilly')
elif Fahrenheit<90:
    print('It is OK')
else:
    print('It is hot')
