'''
An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, A, of size N, 
each memory location has some unique index, i (where 0 <= i < N), that can be referenced as A[i] or Ai.

Reverse an array of integers.

Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

Example

Return .

Function Description

Complete the function reverseArray in the editor below.

reverseArray has the following parameter(s):

int A[n]: the array to reverse
Returns

int[n]: the reversed array
Input Format

The first line contains an integer, , the number of integers in .
The second line contains  space-separated integers that make up .

Constraints

1 <= N <= 10^3

1<= A[i] <= 10^4, where A[i] is the ith integer in A

'''

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    a_copy = []
    
    i = -2
    for element in a:
        a_copy.append(a[i + 1])
        i -= 1

    return a_copy