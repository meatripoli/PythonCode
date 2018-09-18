def average(list):
    total_number_of_items=len(list)
    add=0
    for integer in list:
        add=add+integer
    average=add/total_number_of_items
    return average
