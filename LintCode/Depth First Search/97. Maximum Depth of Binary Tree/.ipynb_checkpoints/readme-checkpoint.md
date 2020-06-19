Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
```
Input: tree = {}
Output: 0
Explanation: The height of empty tree is 0.
```
Example 2:
```
Input: tree = {1,2,3,#,#,4,5}
Output: 3	
Explanation: Like this:
   1
  / \                
 2   3                
    / \                
   4   5
it will be serialized {1,2,3,#,#,4,5}
```
### Notice
The answer will not exceed `5000`