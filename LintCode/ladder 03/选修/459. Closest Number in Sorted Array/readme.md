Given a target number and an integer array A sorted in ascending order, find the index `i` in A such that A[i] is closest to the given target.

Return -1 if there is no element in the array.

# Example
## Example 1:
```
Input: [1, 2, 3] , target = 2
Output: 1.
```
Example 2:
```
Input: [1, 4, 6], target = 3
Output: 1.
```
Example 3:
```
Input: [1, 4, 6], target = 5,
Output: 1 or 2.
```
# Challenge
O(logn) time complexity.

# Notice
There can be duplicate elements in the array, and we can return any of the indices with same value.