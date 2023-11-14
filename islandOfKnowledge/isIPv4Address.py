""" 
An IP address is a numerical label assigned to each device 
(e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.
"""

import re

def isIPv4Address(inputString):
  numbersArray = inputString.split('.')
  hasFourSetsOfNumbers = len(numbersArray) == 4

  if hasFourSetsOfNumbers is False: 
    return False
  
  hasCorrectNumberCountInEachSpot = (len(numbersArray[0]) >= 1 and len(numbersArray[1]) >= 1 and len(numbersArray[2]) >= 1) and len(numbersArray[3]) >= 1

  if hasCorrectNumberCountInEachSpot is False: 
    return False

  isNumbers = numbersArray[0].isdigit() and numbersArray[1].isdigit() and numbersArray[2].isdigit() and numbersArray[3].isdigit()


  if isNumbers is False:
    return False
  
  # regular expression (re) to make replacement of each number element
  numbersArray = [number for number in numbersArray if number != '' and number != '00' and number != '01' and not re.search('[^0-9]', number)]
  
  if len(numbersArray) != 4:
    return False

  notBinaryNums = []
  # notBinaryNums = [number for number in numbersArray if int(number) > 255 or int(number) < 0]
  for number in numbersArray:
    if int(number) > 255 or int(number) < 0:
       notBinaryNums.append(number)

  if len(notBinaryNums) == 0:
    return True
  else:
    return False
