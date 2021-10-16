/*
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

For

picture = ["abc",
           "ded"]

the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]

*/


function addBorder(picture: string[]): string[] {
    const newPicture: string[] = picture.map((ele) => {
        return '*' + ele + '*';
    });
    let numberOfAsterisks = picture[0].length + 2;
    newPicture.unshift('');
    newPicture.push('');
    for(let i = 0; i < numberOfAsterisks; i++) {
        newPicture[0] += '*'
        newPicture[newPicture.length - 1] += '*';
    }
    return newPicture;
}