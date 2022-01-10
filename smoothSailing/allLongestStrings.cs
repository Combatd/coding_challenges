/*
#allLongestStrings

Given an array of strings, return another array containing all of its longest strings.
*/

/*
WhiteBoard
* Initialize a new string array to hold the longest strings.
    - string[] longestStrings
* I think I will need a variable to track the highest length of all strings in the array.
    - int longestLength will initialize at 0
* I should loop through and grab all the string lengths, and update the longestLength if the current string's Length is longer than the longestLength variable
    - inputArray[i].Length will be checked on each iteration
* a second loop may be needed to grab all the strings that have a Length property maching longestLength
    - push each of them into the longestStrings array
* return longestStrings

Time: O(2n) = O(n)
*/

using System;
using System.Collections.Generic;

namespace arcade 
{
    public class SmoothSailing 
    {

        string[] allLongestStrings(string[] inputArray) 
        {
            var longestStrings = new List<string> { };
            int longestLength = 0;

            // loop to find longestLength
            for(int i = 0; i < inputArray.Length; i++) {
                bool currentStringLengthisGreaterThanLongestLength() {
                    return inputArray[i].Length > longestLength;
                } 
                if(currentStringLengthisGreaterThanLongestLength()) {
                    longestLength = inputArray[i].Length;
                }
            }


            // loop through to grab strings matching longestLength
            for (int j = 0; j < inputArray.Length; j++) {
                bool currentStringMatchesLongestLength() {
                    return inputArray[j].Length == longestLength;
                }
                if (currentStringMatchesLongestLength()) {
                    longestStrings.Add(inputArray[j]);
                }
                
            }
            return longestStrings.ToArray();
        }

    }

}

