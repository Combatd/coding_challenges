'''
Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''

'''
Whiteboarding

* I can assume that both inputs, a and b, are integers.
* Both positive and negative numbers can be handled with arithmetic operators.
* I will use the print keyword to output each arithmetic operation.
* str keyword converts integer to string

Possible Test Case:
a = 3
b = 5

outputs
8
-2
15

'''

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(str(a + b))
print(str(a - b))
print(str(a * b))