Write a program to find the node at which the intersection of two singly linked lists begins.

# Example
## Example 1:
```
Input:
	A:          a1 → a2
	                   ↘
	                     c1 → c2 → c3
	                   ↗            
	B:     b1 → b2 → b3
Output: c1
Explanation ：begin to intersect at node c1.
```
Example 2:
```
Input:
Intersected at 6
1->2->3->4->5->6->7->8->9->10->11->12->13->null
6->7->8->9->10->11->12->13->null
Output: Intersected at 6
Explanation：begin to intersect at node 6.
```
# Challenge
Your code should preferably run in O(n) time and use only O(1) memory.

# Notice
- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.