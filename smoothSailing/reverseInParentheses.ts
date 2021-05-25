/*
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim"
*/

function reverseInParentheses(inputString: string): string {
    let firstPar: number = 0;
    let secondPar: number = 0;
    const alphabetExp = /[a-zA-Z]/g;

    if(!alphabetExp.test(inputString)) {
        return '';
    }

    firstPar = inputString.indexOf('(')
    secondPar = inputString.indexOf(')')

    if(firstPar === -1 || secondPar === -1) {
        return inputString;
    } else if (firstPar === 0 && secondPar === inputString.length - 1) {
        return inputString.slice(firstPar + 1, secondPar).split('').reverse().join('');
    }


    let stuff = inputString.slice(firstPar + 1, secondPar - 1).split('').reverse().join('');
    return inputString.slice(0, firstPar - 1) + stuff + inputString.slice(secondPar + 1);
 }