#!/bin/python3

import math
import os
import random
import re
import sys

'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

alison heck -> Alison Heck

Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, S.

Constraints

* 0 < len(S) < 1000
* The string consists of alphanumeric characters and spaces

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, S.

Sample Input

chris alan
Sample Output

Chris Alan

'''

'''
Whiteboarding

* Since the string S contains alphanumeric characters and spaces, I won't have to filter out weird characters !@#$
* I can use String.split(' ') to split first and last names to array by whitespace.
* I should target the first character in each array element
* I should be able to concatenate the full name back into a string
'''


# Complete the solve function below.
def solve(s):
    first_and_last_name = s.split(' ') # split into array by whitespace
    full_name = []
    for name in first_and_last_name:
        full_name.append(name.capitalize())
     
    return ' '.join(full_name)