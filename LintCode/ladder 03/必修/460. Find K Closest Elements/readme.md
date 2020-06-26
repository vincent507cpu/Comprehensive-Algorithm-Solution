Given `target`, a non-negative integer `k` and an integer array `A` sorted in ascending order, find the `k` closest numbers to `target` in `A`, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example 1:
```
Input: A = [1, 2, 3], target = 2, k = 3
Output: [2, 1, 3]
```
Example 2:
```
Input: A = [1, 4, 6, 8], target = 3, k = 3
Output: [4, 1, 6]
```
### Challenge
O(logn + k) time

### Notice
1. The value k is a non-negative integer and will always be smaller than the length of the sorted array.
2. Length of the given array is positive and will not exceed 10^410
3. Absolute value of elements in the array will not exceed 10^410