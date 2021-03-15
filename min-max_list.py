#Task: Write a function that returns both the minimum and maximum number of the given list/array. 
#The exercise gives only non-empty lists as arguments

def min_max(lst):
    return [min(lst), max(lst)]


#but, if didn't could be simply handled like this:
# def min_max(lst):
#     try:
#         return [min(lst), max(lst)]
#     except ValueError:
#         print("Can't look for the minimum and maximum in a empty array!")
#         return -1
#     except TypeError:
#         print("Please pass a array as argument.")
#         return -1


#Another solution:
# def min_max(lst):
#     try:
#       max = lst[0]
#       min = lst[0]
#       for i in lst:
#       if i > max:
#           max = i
#       if i < min:
#           min = i
#       print(f'Maximum: {max}, Minimum: {min}')
#       return max, min
#     except ValueError:
#         print("Can't look for the minimum and maximum in a empty array!")
#         return -1
#     except TypeError:
#         print("Please pass a array as argument.")
#         return -1


#Given tests in codewars exercise:
# test.assert_equals(min_max([1,2,3,4,5]), [1, 5])
# test.assert_equals(min_max([2334454,5]), [5, 2334454])