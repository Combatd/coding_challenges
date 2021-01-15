// Given an integer n, return the largest number that contains 
// exactly n digits.

function largestNumber(n) {
    let integerString = "";
    for (let i = 0; i < n; i++ ) {
        integerString += "9"; // concatenate number 9 as it is the largest single digit
    }
    return Number(integerString); // convert the String to Number type
}

console.log(largestNumber(3));
console.log(largestNumber(2));