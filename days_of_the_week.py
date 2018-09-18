user_response = input('Enter a number between 1 and 7')
number = int(user_response)
days = [ 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
if number<7:
    print(days[number-1])
else:
    print ('There are no more days in the week')
