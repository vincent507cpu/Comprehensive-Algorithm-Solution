Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Example 1:
```
Input: [0]
Output:
[
  [],
  [0]
]
```
Example 2:
```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```
### Challenge
Can you do it in both recursively and iteratively?

### Notice
- Each element in a subset must be in non-descending order.
- The ordering between two subsets is free.
- The solution set must not contain duplicate subsets.