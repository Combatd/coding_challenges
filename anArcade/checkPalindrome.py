# Given the string, check if it is a palindrome.

def checkPalindrome(inputString):
    reversedString = inputString[::-1] # slice the string backwards
    return inputString == reversedString