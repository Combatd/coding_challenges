import math
import os
import random
import re
import sys

'''
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
'''

if __name__ == '__main__':
    n = int(raw_input().strip())