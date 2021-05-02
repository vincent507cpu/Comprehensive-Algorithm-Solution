# Description
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

> The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
> The number of nodes does not exceed 20.
# Example
## Example 1:
```
Input:

tree = {1,2,3}
Output:

[[1],[2,3]]
Explanation:

   1 
  / \ 
 2   3 
it will be serialized {1,2,3}
```
## Example 2:
```
Input:

tree = {1,#,2,3} 
Output:

[[1],[2],[3]] 
Explanation:

1 
 \ 
  2 
 / 
3 
it will be serialized {1,#,2,3}
```
# Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.