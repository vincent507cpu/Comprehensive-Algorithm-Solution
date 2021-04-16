Implement regular expression matching with support for `'.'` and `'*'`.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


The function prototype should be:

bool isMatch(string s, string p)

isMatch("aa","a") → false

isMatch("aa","aa") → true

isMatch("aaa","aa") → false

isMatch("aa", "a*") → true

isMatch("aa", ".*") → true

isMatch("ab", ".*") → true

isMatch("aab", "c*a*b") → true

# Example
## Example 1:
```
Input："aa"，"a"
Output：false
Explanation：
unable to match
```
Example 2:
```
Input："aa"，"a*"
Output：true
Explanation：
'*' can repeat a
```