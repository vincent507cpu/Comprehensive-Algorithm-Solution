Given a string `s` and a set of `n` substrings. You are supposed to remove every instance of those n substrings from s so that s is of the minimum length and output this minimum length.

# Example
## Example 1:
```
Input:
"ccdaabcdbb"
["ab","cd"]
Output:
2
Explanation: 
ccdaabcdbb -> ccdacdbb -> cabb -> cb (length = 2)
```
Example 2:
```
Input:
"abcabd"
["ab","abcd"]
Output:
0
Explanation: 
abcabd -> abcd -> "" (length = 0)
```