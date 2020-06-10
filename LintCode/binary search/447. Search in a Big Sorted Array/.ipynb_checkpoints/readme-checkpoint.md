Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by `ArrayReader.get(k)` (or ArrayReader->get(k) for C++).

Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example 1:
```
Input: [1, 3, 6, 9, 21, ...], target = 3
Output: 1
```
Example 2:
```
Input: [1, 3, 6, 9, 21, ...], target = 4
Output: -1
```
### Challenge
O(logn) time, n is the first index of the given target number.

### Notice
If you accessed an inaccessible index (outside of the array), ArrayReader.get will return `2,147,483,647`.