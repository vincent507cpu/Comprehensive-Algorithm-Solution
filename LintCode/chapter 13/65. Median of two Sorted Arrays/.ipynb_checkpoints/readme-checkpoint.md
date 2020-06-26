There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

Example 1
```
Input:
A = [1,2,3,4,5,6]
B = [2,3,4,5]
Output: 3.5
```
Example 2
```
Input:
A = [1,2,3]
B = [4,5]
Output: 3
```
### Challenge
The overall run time complexity should be `O(log (m+n))`.

### Clarification
- The definition of the median:
- The median here is equivalent to the median in the mathematical definition.
- The median is the middle of the sorted array.
- If there are n numbers in the array and n is an odd number, the median is `A[(n-1)/2]`.
- If there are n numbers in the array and n is even, the median is `(A[n / 2] + A[n / 2 + 1]) / 2`.
- For example, the median of the array `A=[1,2,3]` is 2, and the median of the array `A=[1,19]` is 10.