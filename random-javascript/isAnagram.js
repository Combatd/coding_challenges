/*
    ## 1) Given two strings, return true if they are anagrams of one another

Anagram: A word or phrase formed by reordering the letters of another word or phrase, such as `add` and `dad`.
*/

const isAnagram = (word1, word2) => {
    if (word1.split('').sort().join() == word2.split('').sort().join()) {
        return true;
    }
    return false;
}

/*
Given an array of words have your function group the words which are anagrams next to each other.

Example: [car, rats, arc, star] → [rats, star, arc, car]
*/
const areAnagrams = (wordArray) => {
    // hold each Anagram as a key
    const anagrams = {}
    const anagramArray = []
    wordArray.forEach(word => {
        key = word.split('').sort().join(); // we have to keep rearranging by individual characters
        if (key in anagrams) {
            anagrams[key].push(word); // add to the end of it
        } else {
            anagrams[key] = [word] // will be in the array
        }
    });
    anagramArray.push(Object.values(anagrams).join().split(','));
    return anagramArray
}

console.log(areAnagrams(['car', 'rats', 'arc', 'star']))