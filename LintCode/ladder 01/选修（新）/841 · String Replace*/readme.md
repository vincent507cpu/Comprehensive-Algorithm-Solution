# Description
Given two identical-sized string array `A`, `B` and a string `S`. All substrings `A` appearing in `S` are replaced by `B`.(Notice: From left to right, it **must** be replaced if it can be replaced. If there are multiple alternatives, replace longer priorities. After the replacement of the characters can't be replaced again.)

> - The size of each string array does not exceed 100, the total string length does not exceed 50000.
> - The lengths of A [i] and B [i] are equal.
> - The length of S does not exceed 50000.
> - All characters are lowercase letters.
> - We guarantee that the A array does not have the same string

# Example
## Example 1
```
Input:
A = ["ab","aba"]
B = ["cc","ccc"]
S = "ababa"

Output: "cccba"
Explanation: In accordance with the rules, the substring that can be replaced is "ab" or "aba". Since "aba" is longer, we replace "aba" with "ccc".
```
## Example 2
```
Input:
A = ["ab","aba"]
B = ["cc","ccc"]
S = "aaaaa"

Output: "aaaaa"
Explanation: S does not contain strings in A, so no replacement is done.
```
## Example 3
```
Input:
A = ["cd","dab","ab"]
B = ["cc","aaa","dd"]
S = "cdab"

Output: "ccdd"
Explanation: From left to right, you can find the "cd" can be replaced at first, so after the replacement becomes "ccab", then you can find "ab" can be replaced, so the string after the replacement is "ccdd".
```