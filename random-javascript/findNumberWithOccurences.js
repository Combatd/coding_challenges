function findNumberWithNOccurrences(numbers, n) {
    let denomOccurences = {} // object (hashmap)
    for(let i = 0; i < numbers.length; i++) {
        if (!denomOccurences[numbers[i]]) {
            denomOccurences[numbers[i]] = 1; // currently undefined
        } else {
            denomOccurences[numbers[i]] += 1; // iterate if already there
        }
        
    }
    const denomKeys = Object.keys(denomOccurences);
    for(let i = 0; i < denomKeys.length; i++) {
        if(denomOccurences[denomKeys[i]] === n) {
            return denomKeys[i];
        } 
    }
 }