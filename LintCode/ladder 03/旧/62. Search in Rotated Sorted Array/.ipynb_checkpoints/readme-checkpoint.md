Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example 1:
```
Input: [4, 5, 1, 2, 3] and target=1, 
Output: 2.
```
Example 2:
```
Input: [4, 5, 1, 2, 3] and target=0, 
Output: -1.
```
### Challenge
O(logN) time