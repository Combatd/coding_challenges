/*
Two arrays are called similar if one can be obtained from another by swapping at most 
one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.
*/

function areSimilar(a: number[], b: number[]): boolean {
    let isSimilar: boolean = true; // we will return this
    let aVal = null; // the value from a
    let bVal = null; // the value from b
    let swapped: boolean = false; // track if we swapped the elements already
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) { // We won't swap the same elements
        if (aVal === null || bVal === null) {
          aVal = a[i]; bVal = b[i]; // assign so the values aren't null
        } else {
          if (swapped || aVal !== b[i] || bVal !== a[i]) { // We can't swap more than once or have the next element different in one of the arrays
            isSimilar = false;
          }
          swapped = true; // all the checks have passed!
        }
      }
    }
    return isSimilar;
}