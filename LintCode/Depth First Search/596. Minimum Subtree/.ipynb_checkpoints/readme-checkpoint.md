Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.


Example 1:
```
Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
The sum of whole tree is minimum, so return the root.
```
Example 2:
```
Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
```
### Notice
LintCode will print the subtree which root is your return node.

It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.