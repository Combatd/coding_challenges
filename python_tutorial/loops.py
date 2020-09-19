'''
Task
The provided code stub reads an integer, n, from STDIN. For all non-negative integers i < n, print i^2.

Example

n = 3

The list of non-negative integers that are less than n = 3 is [0,1,2]. Print the square of each number on a separate line.

0
1
4
'''
'''
Whiteboarding

* The value of n is above 0.
* The first line we print will contain only 0.
* We will print n number of lines, each line corresponding to i.
* On each line i, we will output i^2
* This can be solved by utilizing a for-in loop.
* i will represent each element in a range of 0 to n, excluding n.
'''


if __name__ == '__main__':
    n = int(input())
    print(0)
    for i in range(1, n):
        print(i * i)