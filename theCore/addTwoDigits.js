function addTwoDigits(n) {
    let digitString = n.toString(); // convert to string
    let digitArray = digitString.split(""); // split the 2 chars into array
    let sumOfTwoDigits = 0; // accumulator to return
    digitArray.forEach(integer => {
        sumOfTwoDigits += Number(integer); // convert the string to Number type
    });
    return sumOfTwoDigits;
}

console.log(addTwoDigits("12")); // 3
console.log(addTwoDigits("45")); // 9