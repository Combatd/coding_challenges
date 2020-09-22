'''
The included code stub will read an integer, n, from STDIN.

Without using any string methods, try to print the following:

123...n

Note that "..." represents the consecutive values in between.

Example
n = 5

Print the string 12345.

Input Format

The first line contains an integer n.
'''

'''
Whiteboarding
* I can assume the n argument being passed in is an integer.
* With a for in loop, I will print each number i through range 1 through n
    * I will use the end option to nest the i inside ""
* Finally, I will print the n with the end option, which is not included in the for in loop.
* Complexity Analysis:
    * Space = O(n) Linear
    * Time = O(n) Linear
'''

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n):
        print(i, end="")
        
    print(n)