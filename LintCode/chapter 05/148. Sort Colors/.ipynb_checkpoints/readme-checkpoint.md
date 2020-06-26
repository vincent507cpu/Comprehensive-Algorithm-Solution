Given an array with n objects colored *red*, *white* or *blue*, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers `0`, `1`, and `2` to represent the color red, white, and blue respectively.

Example 1
```
Input : [1, 0, 1, 2]
Output : [0, 1, 1, 2]
Explanation : sort it in-place
```
Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?