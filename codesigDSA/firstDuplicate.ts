/*
Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, 
return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. 
If there are no such elements, return -1.
*/

function solution(a: number[]): number {
    let index: number = a.length - 1;
    const existingNumbersSet: Set<number> = new Set(); // keep track of numbers using set or linked list
    let firstDuplicate: number = -1;

    while(index >= 0) {
        if (existingNumbersSet.has(a[index])) {
            firstDuplicate = index
        } else {
            existingNumbersSet.add(a[index]);
        }
        index--
    }

    if (firstDuplicate !== -1) {
        return a[firstDuplicate];
    } else {
        return -1;
    }
}