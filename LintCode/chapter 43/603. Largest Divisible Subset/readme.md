Given a set of `distinct positive` integers, find the largest subset such that every pair `(Si, Sj)` of elements in this subset satisfies: `Si % Sj = 0` or `Sj % Si = 0`.

# Example
## Example 1:
```
Input: nums =  [1,2,3], 
Output: [1,2] or [1,3]
```
Example 2:
```
Input: nums = [1,2,4,8], 
Output: [1,2,4,8]
```
# Notice
If there are multiple solutions, return any subset is fine.
$1 \leq len(nums) \leq 500001≤len(nums)≤50000$