def _remove_trailing_whitespace(string):
    my_index = None
    for x in range(-1,-(len(string)),-1):
        if string[x] != " ":
            my_index = x
            break
    # slice the string from that index to the end
    new_string = string[0:my_index+1]
    return new_string


#def _remove_trailing_whitespace_sample_(string):
#    my_index = None
#    i = len(string)
#    while i > 0:
#        if string[i-1] != " ":
#            my_index = i
#            break
#        i = i - 1
#    # slice the string from 0 to that index
#    new_string = string[:my_index]
#    return new_string
