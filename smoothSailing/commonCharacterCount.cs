/*
#commonCharacterCount

Given two strings, find the number of common characters between them.

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".


[execution time limit] 3 seconds (cs)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer

*/

using System;
using System.IO;
using System.CodeDom.Compiler;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text;
using SimpleJson.Reflection;

using System.Text.RegularExpressions;
using System.Linq;
using System.Threading;

namespace arcade {

    public class SmoothSailing {

        int commonCharacterCount(string s1, string s2) {
            int amountOfCommonCharacters = 0; // accumulator

            // split all the characters of both strings s1 and s2
            string[] arr1 = s1.Split("");
            string[] arr2 = s2.Split("");

            List<string> strings1 = new List<string>(arr1);
            List<string> strings2 = new List<string>(arr2);

            // loop over the first string list to get the index of a matcher
            for (int i = 0; i < strings1.Count; i++) {
                int secondIndex = strings2.IndexOf(strings1[i]);
                // if we have a match, add 1 to amountOfCommonCharacters, and remove the index so that we don't count it twice
                if (strings2.Contains(strings1[i])) {
                    strings2.RemoveAt(secondIndex);
                    amountOfCommonCharacters++;
                }
            }

            return amountOfCommonCharacters;
        }

    }
}