user_response=input('Write a number: ')
number=float(user_response)
guess=number/2
iteration=0
while abs(number-guess**2)>0.01:
    print('Iteration', iteration, 'Guessed squared root is: ', guess)
    guess=(guess+(number/guess))/2
    iteration=iteration+1
print('DONE')
print('Original number is: ',number)
print('Square root is: ',guess)
