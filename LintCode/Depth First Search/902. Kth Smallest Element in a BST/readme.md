Given a binary search tree, write a function `kthSmallest` to find the kth smallest element in it.


Example 1:
```
Input：{1,#,2},2
Output：2
Explanation：
	1
	 \
	  2
The second smallest element is 2.
```
Example 2:
```
Input：{2,1,3},1
Output：1
Explanation：
  2
 / \
1   3
The first smallest element is 1.
```
### Challenge
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Notice
You may assume k is always valid, `1 ≤ k ≤ BST's total elements`.