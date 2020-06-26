Given an array `nums` of integers and an int `k`, partition the array (i.e move the elements in "nums") such that:

All elements < `k` are moved to the left
All elements >= `k` are moved to the right
Return the partitioning index, i.e the first index `i` `nums[i] >= k`.

Example 1:
```
Input:
[],9
Output:
0
```
Example 2:
```
Input:
[3,2,2,1],2
Output:1
Explanation:
the real array is[1,2,2,3].So return 1
```
### Challenge
Can you partition the array in-place and in O(n)?