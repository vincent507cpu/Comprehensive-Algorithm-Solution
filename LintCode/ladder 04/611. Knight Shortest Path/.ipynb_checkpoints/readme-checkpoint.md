Given a knight in a chessboard (a binary matrix with `0` as empty and `1` as barrier) with a `source` position, find the shortest path to a `destination` position, return the length of the route.

Return `-1` if destination cannot be reached.

Example 1:
```
Input:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output: 2
Explanation:
[2,0]->[0,1]->[2,2]
```
Example 2:
```
Input:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] 
Output:-1
```
### Clarification
If the knight is at (x, y), he can get to the following positions in one step:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
### Notice
source and destination must be empty.

Knight can not enter the barrier.

Path length refers to the number of steps the knight takes.