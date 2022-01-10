import math

def shapeArea(n):
    if n == 1:
        return 1
    # n^2 + (n - 1)2 , since with n = 2, we had 4 + 1 and n = 3, we had 9 + 4
    return n**2 + (n - 1)**2