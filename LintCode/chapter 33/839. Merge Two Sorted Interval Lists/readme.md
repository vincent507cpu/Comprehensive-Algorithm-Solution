Merge two sorted (ascending) lists of interval and return it as a new sorted list. The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

# Example
## Example1
```
Input: list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)]
Output: [(1,4),(5,6)]
Explanation:
(1,2),(2,3),(3,4) --> (1,4)
(5,6) --> (5,6)
```
Example2
```
Input: list1 = [(1,2),(3,4)] and list2 = [(4,5),(6,7)]
Output: [(1,2),(3,5),(6,7)]
Explanation:
(1,2) --> (1,2)
(3,4),(4,5) --> (3,5)
(6,7) --> (6,7)
```
## Notice
- The intervals in the given list do not overlap.
- The intervals in different lists may overlap.