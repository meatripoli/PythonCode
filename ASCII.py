def ASCII(number,letter):
    x=chr(number) #find character from number
    y=ord(letter) #find number from letter
    return x
    return y

def add_ASCII_numbers(word):
    summ=0
    for item in word:
        x=ord(item)
        summ=summ+x
    return summ
