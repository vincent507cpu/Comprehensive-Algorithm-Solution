A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

# Example
## Example 1:
```
Input: "12"
Output: 2
Explanation: It could be decoded as AB (1 2) or L (12).
```
Example 2:
```
Input: "10"
Output: 1
```
## Notice
we can't decode an empty string. So you should return 0 if the message is empty.
The length of message n \leq 100n≤100