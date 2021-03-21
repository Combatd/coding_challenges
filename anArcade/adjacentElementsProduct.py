# Given an array of integers, find the pair of adjacent elements 
# that has the largest product and return that product.

def adjacentElementsProduct(inputArray):
    largestProduct = inputArray[0] * inputArray[1]
    idx = 0
    for number in inputArray:
        if idx == len(inputArray) - 1: # if number is last element in the list
            break

        if number * inputArray[idx + 1] > largestProduct:
            largestProduct = number * inputArray[idx + 1]

        idx += 1 # iterate idx before next step in loop

    return largestProduct