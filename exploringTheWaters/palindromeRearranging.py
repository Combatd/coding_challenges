""" 
Given a string, find out if its characters can be rearranged to form a palindrome.
"""

def palindromeRearranging(inputString):
  letter_dict = {}

  for letter in inputString:
    if letter_dict.get(letter) == None:
      letter_dict[letter] = 1
    else:
      letter_dict[letter] += 1
  
  letterWasOdd = False
  for letter_count in letter_dict.values():
    if letter_count % 2 != 0:
      if letterWasOdd: 
        return False
      else: 
        letterWasOdd = True

  return True