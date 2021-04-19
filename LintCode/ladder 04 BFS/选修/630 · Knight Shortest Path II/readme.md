# Description
Given a knight in a chessboard `n * m` (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position is `(0, 0)` and he wants to reach position `(n - 1, m - 1)`, Knight can only be from left to right. Find the shortest path to the destination position, return the length of the route. Return `-1` if knight can not reached.

#  Clarification
If the knight is at (x, y), he can get to the following positions in one step:
```
(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
```
# Example
## Example 1:
```
Input:
[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
Output:
3
Explanation:
[0,0]->[2,1]->[0,2]->[2,3]
```
## Example 2:
```
Input:
[[0,1,0],[0,0,1],[0,0,0]]
Output:
-1
```