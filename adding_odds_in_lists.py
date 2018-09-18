def adding_odds_of_two_lists(A,B):
    sum_of_odd=0
    a_plus_b=A+B
    for item in a_plus_b:
        if item%2!=0:
            sum_of_odd=sum_of_odd+item
    return sum_of_odd
