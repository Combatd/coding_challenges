/*
Some people are standing in a row in a park. 
There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
People can be very tall!

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
*/

function sortByHeight(a: number[]): number[] {
    const negativeOneIndex: Array<number> = [];
    const sortedNumberArray: Array<number> = [];
    for (let i = 0; i < a.length; i++) {
        if (a[i] < 0) {
            negativeOneIndex.push(i); // push the index of the current -1
        } else {
            sortedNumberArray.push(a[i]); // push the current element in the new array
        }
    }

    sortedNumberArray.sort( (a, b) => a - b ); // sort the new array that has -1 removed
    negativeOneIndex.forEach( (index) => {
        sortedNumberArray.splice(index, 0, -1); // splice into the specific index of sortedNumberArray
    })
    return sortedNumberArray;
}