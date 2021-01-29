function compressedString(message) {
    // Write your code here
    let characterCount = {}; // object (dictionary to store d letters)
    let compressedString = '';

    // maybe we should add key value pairs for these letters
    for (let i = 0; i < message.length; i++) {
        if (characterCount[i] != false) { 
            
            if (characterCount[message[i]] != Number(characterCount[message[i]])) {
                characterCount[message[i]] = 1;
            } else {
                characterCount[message[i]] += 1;
            }

        }
    }

    let uniqueCharsString = message.split('').filter(function(item, pos, self) {
        return self.indexOf(item) == pos;
    })
    .join('');

    for (let j = 0; j < message.length; j++) {
        let count = letterCount(message, message[j]);
        if (count > 1) {
            compressedString += `${message[j]}${count}`;
        } else {
            compressedString += message[j];
        }
    }

    return compressedString;
}

function letterCount(string, char) {
    let count = 0;

    for (let i = 0; i < string.length; i++) {
        if (string[i] === char) {
            count += 1;
        }
    }

    return count;
}