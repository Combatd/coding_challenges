'''
Given a sequence of integers as an array, 
determine whether it is possible to obtain a strictly increasing 
sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. 
Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. 
Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
'''

def almostIncreasingSequence(sequence):
    # Check for duplicate values
    if len(sequence) != len(set(sequence)):
        return False

    index = 0 # iterate on each iteration of loop
    removedNumber = False # Is a number already removed
    for number in sequence:
        if number >= sequence[index + 1]:
            if removedNumber == True:
                return False
            else:
                sequence.remove(number)
                removedNumber = True
        index += 1
        if len(sequence) > index: # make sure not jumping out of the list
            break

    # Check the mutated sequence in reversed order
    reversed_sequence = sequence[::-1] # slice operator
    sub_index = 0
    for number in reversed_sequence:
        if number < reversed_sequence[sub_index + 1]:
            if removedNumber == True:
                return False
            else:
                reversed_sequence.remove(number)
                removedNumber = True
        sub_index += 1
        if len(reversed_sequence) > sub_index: # make sure not jumping out of the list
            break

    
    # # Use set() to only grab unique values, then compare to the list
    # if len(reversed_sequence) != len(set(reversed_sequence)):
    #     return False

    return True