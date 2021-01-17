'''
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
each statue having an non-negative integer size. Since he likes to make things perfect, 
he wants to arrange them from smallest to largest so that each statue will be bigger 
than the previous one exactly by 1. 
He may need some additional statues to be able to accomplish that. 
Help him figure out the minimum number of additional statues needed.

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
'''

def makeArrayConsecutive2(statues):
    sortedStatues = sorted(statues)
    lowest = sortedStatues[0]
    highest = sortedStatues[-1]
    statues_needed = 0
    
    for index in range(lowest, highest + 1): # need to include the highest size
        if index not in sortedStatues:
            statues_needed += 1
    
    return statues_needed