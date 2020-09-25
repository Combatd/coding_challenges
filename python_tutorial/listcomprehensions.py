'''
Let's learn about list comprehensions! 
You are given three integers x, y and z 
representing the dimensions of a cuboid along with an integer. 
Print a list of all possible coordinates given by (i,j,k) 
on a 3D grid where the sum of i + j + k is not equal to n. 
Here, 0 <= i <= x; 0<= j <= y; 0 <= k <= z. 

Please use list comprehensions rather than multiple loops, as a learning exercise.
'''

'''
Input Format
Four integers x, y, z, and n, each on a separate line.

Constraints
Print the list in lexicographic increasing order.

Sample Input 0
1
1
1
2

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Explanation 0
Each variable x,y,z will have values of 0 or 1. 
All permutations of lists in the form [i,j,k]
Remove all arrays that sum to n = 2 to leave only the valid permutations.
'''

'''
Whiteboarding
* I should build out the condition to check x, y, z do not sum to n
* I can use a list comprehension (instead of Array.map) to return new lists for each valid permuation i, j, k passing the conditional check above.
* I could use for in loop with range inside the list comprehension.
'''

import math


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    def sum_three_nums(i,j,k):
        return ''


    permutations = [] # list will hold lists of integers