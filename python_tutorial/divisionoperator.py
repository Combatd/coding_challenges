'''
Task
The provided code stub reads two integers, a and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division,  a/b .

No rounding or formatting is necessary.

Example

The result of the integer division 3//5 = 0 .
The result of the float division 3/5 = 0.6 .

Whiteboarding
* We can assume that both a and b will be passed in as integers.
* We will use the division operator / to return an integer and // to return a float.
* The results of a//b and a/b will be printed on their own lines.
* I do not require special formatting or rounding of numbers.
* I should make sure that b is not 0, which would be impossible

'''

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

if b == 0: 
    print('b cannot be 0')
else:
    print(a//b)
    print(a/b)