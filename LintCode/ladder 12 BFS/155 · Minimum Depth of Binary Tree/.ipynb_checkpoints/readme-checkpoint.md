# Description
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Example
## Example 1:
```
Input: {}
Output: 0
```
```
## Example 2:
```
Input:  {1,#,2,3}
Output: 3	
Explanation:
	1
	 \ 
	  2
	 /
	3    
it will be serialized {1,#,2,3}
```
## Example 3:
```
Input:  {1,2,3,#,#,4,5}
Output: 2	
Explanation: 
      1
     / \ 
    2   3
       / \
      4   5  
it will be serialized {1,2,3,#,#,4,5}
```