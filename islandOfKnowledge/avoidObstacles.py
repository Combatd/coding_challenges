""" 
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. 
You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

inputArray = [5, 3, 6, 7, 9]
solution is 4
"""

def avoidObstacles(inputArray):
  # if avoiding certain numbers as obstacles, we should have the array(list) sorted ascending
  inputArray.sort()

  # We have to start with jumps of a distance of 1.
  jumpDistance = 1
  
  # If the obstacle positions are divisible by our jump distance, we will hit an obstacle.
  while(distanceIsDivisibleByObstaclePosition(inputArray, jumpDistance)):
    jumpDistance += 1

  return jumpDistance

def distanceIsDivisibleByObstaclePosition(inputArray, distance):
  for i in range(0, len(inputArray)):
    if inputArray[i] % distance == 0:
      return True
  return False