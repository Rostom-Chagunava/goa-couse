# Given a set of numbers, return the additive inverse of each.
# Each positive becomes negatives, and the negatives become positives
def invert(lst):
    
    my_arr = []
    for i in lst:
        if i >0:
            my_arr.append(-i)
        else :
            my_arr.append(i*-1)
    return my_arr 