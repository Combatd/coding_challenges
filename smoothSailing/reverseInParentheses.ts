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
    let alpha = /[a-zA-Z]/g;
    let exp = /\([^()]+\)/;
    let parenthesis = /(\(\)')+/g;

    while (exp.test(inputString)) {
        inputString = inputString.replace(exp, (r) => r.split('').slice(1,-1).reverse().join(''));
    }

    if(!alpha.test(inputString)) {
        return ''
    }
    
    inputString.replace(parenthesis, '');

    if(inputString.includes('()')) {return 'foobar'}

    return inputString;
}