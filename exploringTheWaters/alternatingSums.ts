
/*
Several people are standing in a row and need to be divided into two teams. 
The first person goes into team 1, 
the second goes into team 2, the third goes into team 1 again, 
the fourth into team 2, and so on.

You are given an array of positive integers - 
the weights of the people. Return an array of two integers, 
where the first element is the total weight of team 1, 
and the second element is the total weight of team 2 after the division is complete.

Example
For a = [50, 60, 60, 45, 70], the output should be
alternatingSums(a) = [180, 105].
*/


function alternatingSums(a: number[]): number[] {
    let midPoint: number = Math.floor(a.length / 2);
    let firstTeam: number = 0;
    let secondTeam: number = 0;

    for(let i = 0; i < a.length; i+=2) {
        firstTeam += a[i];
    }
    for(let j = 1; j < a.length; j+=2) {
        secondTeam += a[j];
    }
    return [firstTeam, secondTeam];
}