# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0. daviti


def find_average(numbers):    
    if not numbers:
        return 0
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average  