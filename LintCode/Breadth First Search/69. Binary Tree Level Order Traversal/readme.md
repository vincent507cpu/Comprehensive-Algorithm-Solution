Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example 1:
```
Input：{1,2,3}
Output：[[1],[2,3]]
Explanation：
  1
 / \
2   3
it will be serialized {1,2,3}
level order traversal
```
Example 2:
```
Input：{1,#,2,3}
Output：[[1],[2],[3]]
Explanation：
1
 \
  2
 /
3
it will be serialized {1,#,2,3}
level order traversal
```
### Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use BFS algorithm to do it.

### Notice
1. The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
2. The number of nodes does not exceed 20.