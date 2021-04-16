Given a boolean 2D matrix, `0` is represented as the sea, `1` is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example 1:
```
Input:
[
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]
]
Output:
3
```
Example 2:
```
Input:
[
  [1,1]
]
Output:
1
```