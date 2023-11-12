""" 
You are given an array of integers. 
On each move you are allowed to increase exactly one of its element by one. 
Find the minimal number of moves required to obtain a strictly increasing sequence from the input. 

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.
"""

def arrayChange(inputArray):
  numberOfMoves = 0
  for integer in inputArray[1:]:
    
    if integer <= inputArray[0] :
      numberOfMoves = numberOfMoves + inputArray[0] - integer + 1
      inputArray[0] = inputArray[0] + 1
    else:
      inputArray[0] = integer
    
  return numberOfMoves
