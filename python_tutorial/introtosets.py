'''
Average = Sum of Distinct Heights / Total Number of Distinct Heights
'''

from functools import reduce

def average(array):
    # your code goes here

    # sum = 0
    # for number in array:
    #     sum += number

    # We can enumerate using a reducer running on all elements
    sum = reduce((lambda x, y: x + y), array)
    return sum / len(array)