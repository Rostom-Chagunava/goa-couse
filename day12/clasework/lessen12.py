# def check_even_or_odd(number):
#     # check if the number is an integer
#     if type(number) != int:
#         return 'Invalid input'
#     return even_or_odd(number) # return the function to check for even or odd
    
# # function to check odd or even
# def even_or_odd(number):
#     if number % 2 == 0:
#         # if value of number is integer returns even
#         return 'Even'
#     # else it should return odd
#     return 'Odd'



# print (check_even_or_odd(int(input("enter your number :"))))    
# def solution(string):
#     my_srting = ""
#     i = len(string)
#     while i > 0:
#         my_srting += string [i-1]
#         i -= 1
#     return my_srting
# print(solution("hallo"))  

# def solution(string):
#    return string [::-1]
# print (solution("etwas"))

# def find_smallest_int(arr):
#     i = 0
#     min = arr[0]
#     while i<len(arr):
#         if arr[i]<min:
#             min = arr[i]
#         i+=1
#     return min
# print (find_smallest_int([2,1,5,4,0,85,96,41,-5]))

# def find_smallest_int(arr):
#     min_number = arr[0]
#     for i in arr:
#         if min_number > i:
#             min_number = i
#     return min_number
# print (find_smallest_int([2,1,5,4,2,85,96,41,-5]))

# def find_smallest_int(arr):
#     smallest = arr[0]
#     for i in range(0,len(arr)):
#         if (arr[i] < smallest):
#             smallest = arr[i]
#     return smallest
# print (find_smallest_int([2,1,5,4,2,85,96,41,-5]))

# def square_sum(numbers):
#     square_s = 0
#     for i in numbers:
#        square_s += i * i

#     return square_s
# print (square_sum([2,2,-5,]))




