""" 
Given an array of integers, 
find the maximal absolute difference between any two of its adjacent elements.

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.
"""

def arrayMaximalAdjacentDifference(inputArray):
  maximumAdjacentDifference = 0 # return value

  for i in range(1, len(inputArray)):
    integer = inputArray[i]

    currentValue = integer 
    prevValue = inputArray[i - 1]

    differenceOfCurrentAndPrev = currentValue - prevValue
    differenceOfPrevAndCurrent = prevValue - currentValue

    if currentValue > prevValue:
      if differenceOfCurrentAndPrev > maximumAdjacentDifference:
        maximumAdjacentDifference = differenceOfCurrentAndPrev
    else:
      if differenceOfPrevAndCurrent > maximumAdjacentDifference:
        maximumAdjacentDifference = differenceOfPrevAndCurrent

  return maximumAdjacentDifference