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

# Wrong, too many lines of code
# def almostIncreasingSequence(sequence):
#     # Check for duplicate values
#     if len(sequence) != len(set(sequence)):
#         return False

#     # edge case - small list
#     if len(sequence) <= 2:
#         return True

#     index = 0 # iterate on each iteration of loop
#     removedNumber = False # Is a number already removed
#     for number in sequence:
#         if number >= sequence[index + 1]:
#             if removedNumber == True:
#                 return False
#             else:
#                 sequence.remove(number)
#                 removedNumber = True
#         index += 1
#         if len(sequence) > index: # make sure not jumping out of the list
#             break

#     # Check the mutated sequence in reversed order
#     reversed_sequence = sequence[::-1] # slice operator
#     sub_index = 0
#     for number in reversed_sequence:
#         if number < reversed_sequence[sub_index + 1]:
#             if removedNumber == True:
#                 return False
#             else:
#                 reversed_sequence.remove(number)
#                 removedNumber = True
#         sub_index += 1
#         if len(reversed_sequence) > sub_index: # make sure not jumping out of the list
#             break

    
#     # # Use set() to only grab unique values, then compare to the list
#     # if len(reversed_sequence) != len(set(reversed_sequence)):
#     #     return False

#     return True

def almostIncreasingSequence(sequence):

    # Edge Case for 1 and two element arrays
    if len(sequence) <= 2:
        return True

    # This would be easier with Memoization...dynamic programming to break up the subproblems

    # Set up a new function to see if it's increasing sequence
    def increasingSequence(test_sequence):
        # Edge case, check if the first element is less than the second for 2 element array
        if len(test_sequence) == 2:
            if test_sequence[0] < test_sequence[1]: # It may already be in ascending order
                return True
        else:
            for i in range(0, len(test_sequence)-1): # loop through a full range
                if test_sequence[i] >= test_sequence[i + 1]: # Make sure there is an increasing sequence
                    return False
                else:
                    pass # skip this iteration of the loop
            return True

    for i in range (0, len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            # Remove current or next element
            test_seq1 = sequence[:i] + sequence[i+1:] # slice operator
            test_seq2 = sequence[:i+1] + sequence[i+2:] # slice operator
            if increasingSequence(test_seq1) == True:
                return True
            elif increasingSequence(test_seq2) == True:
                return True
            else:
                return False # Not an increasing sequence that can be solved with one removal