Partition an unsorted integer array into three parts:

1. The front part < low
2. The middle part >= low & <= high
3. The tail part > high

Return any of the possible solutions.

# Example
## Example 1:
```
Input:
[4,3,4,1,2,3,1,2]
2
3
Output:
[1,1,2,3,2,3,4,4]
Explanation:
[1,1,2,2,3,3,4,4] is also a correct answer, but [1,2,1,2,3,3,4,4] is not
```
Example 2:
```
Input:
[3,2,1]
2
3
Output:
[1,2,3]
```
# Challenge
1. Do it in place.
2. Do it in one pass (one loop).
# Notice
low <= high in all testcases.