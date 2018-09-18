user_response=input('Enter an integer: ')
integer=int(user_response)
iteration=1
factorial=1
while (integer>=iteration):
    factorial=(factorial*(iteration))
    print('Iteration: ',iteration,' multiplication: ',factorial)
    iteration=iteration+1
print(integer,'! is equal to ',factorial)
