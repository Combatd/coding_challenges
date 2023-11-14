""" 
An IP address is a numerical label assigned to each device 
(e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.
"""

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
  
  isValidDigit = str(int(numbersArray[0])) == int(numbersArray[0]) and str(int(numbersArray[1])) == int(numbersArray[1]) and str(int(numbersArray[2])) == int(numbersArray[2]) and str(int(numbersArray[3])) == int(numbersArray[3])
  
  if isValidDigit is False:
    return False

  isBinary = int(numbersArray[0]) <= 255  and int(numbersArray[1]) <= 255  and int(numbersArray[2]) <= 255  and int(numbersArray[3]) <= 255 and int(numbersArray[0]) > -1 and int(numbersArray[1]) > -1  and int(numbersArray[2]) > -1  and int(numbersArray[3]) > -1 

  if isBinary is False: 
    return False
  
  return True
