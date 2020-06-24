Give `n` cities(labeled from `1` to `n`), and the undirected road's `cost` among the cities as a three-tuple `[A, B, c]`(i.e there is a road between city `A` and city `B` and the cost is `c`). We need to find the smallest cost to travel all the cities starting from 1.

Example 1
```
Input: 
n = 3
tuple = [[1,2,1],[2,3,2],[1,3,3]]
Output: 3
Explanation: The shortest path is 1->2->3
```
Example 2
```
Input:
n = 1
tuple = []
Output: 0
```
### Notice
1. A city can only be passed once.
2. You can assume that you can reach all the rest cities.