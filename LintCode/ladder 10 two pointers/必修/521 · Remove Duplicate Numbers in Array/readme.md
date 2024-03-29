# Description
Given an array of integers, remove the duplicate numbers in it.

You should:

1. Do it in place in the array.
2. Put the element after removing the repetition at the beginning of the array.
3. Return the number of elements after removing duplicate elements.
> You don't need to keep the original order of the integers.
# Example
## Example 1:
```
Input:
nums = [1,3,1,4,4,2]
Output:
[1,3,4,2,?,?]
4
```
Explanation:

1. Move duplicate integers to the tail of nums => nums = `[1,3,4,2,?,?]`.
2. Return the number of unique integers in nums => `4`.
3. Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.
## Example 2:
```
Input:
nums = [1,2,3]
Output:
[1,2,3]
3
```
# Challenge
1. Do it in O(n) time complexity.
2. Do it in O(nlogn) time without extra space.