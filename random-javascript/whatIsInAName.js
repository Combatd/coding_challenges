function whatIsInAName(collection, source) {
    var arr = [];
    // Only change code below this line
    const sourceKeys = Object.keys(source); // get all keys of source in an array
    arr = collection.filter((obj) => {
        for (let i = 0; i < sourceKeys.length; i++) {
            if (!obj.hasOwnProperty(sourceKeys[i]) || obj[sourceKeys[i]] !== source[sourceKeys[i]]) {
                return false;
            }
        }
        return true;
    });

    // Only change code above this line
    return arr;
}
  

whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" });