# Description
Given an integers array `A`.

Define `B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]`, calculate B **WITHOUT** divide operation.Out put `B`

# Example
## Example 1
```
Input: A = [1, 2, 3]
Output: [6, 3, 2]
Explanation：B[0] = A[1] * A[2] = 6; B[1] = A[0] * A[2] = 3; B[2] = A[0] * A[1] = 2
```
Example 2
```
Input: A = [2, 4, 6]
Output: [24, 12, 8]
```