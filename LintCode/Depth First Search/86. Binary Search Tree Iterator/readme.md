Design an iterator over a binary search tree with the following rules:

- Elements are visited in ascending order (i.e. an in-order traversal)
- next() and hasNext() queries run in O(1) time in average.

Example 1
```
Input:  {10,1,11,#,6,#,12}
Output:  [1, 6, 10, 11, 12]
Explanation:
The BST is look like this:
  10
  /\
 1 11
  \  \
   6  12
You can return the inorder traversal of a BST [1, 6, 10, 11, 12]
```
Example 2
```
Input: {2,1,3}
Output: [1,2,3]
Explanation:
The BST is look like this:
  2
 / \
1   3
You can return the inorder traversal of a BST tree [1,2,3]
```
### Challenge
Extra memory usage O(h), h is the height of the tree.

**Super Star**: Extra memory usage O(1)