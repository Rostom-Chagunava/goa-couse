# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
def grow(arr):
    mul = 1
    for i in arr:
        mul *= i
    return mul 