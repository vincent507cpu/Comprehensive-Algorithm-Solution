Given a set of candidtate numbers `candidates` and a target number `target`. Find all unique combinations in `candidates` where the numbers sums to `target`.

The same repeated number may be chosen from candidates unlimited number of times.

Example 1:
```
Input: candidates = [2, 3, 6, 7], target = 7
Output: [[7], [2, 2, 3]]
```
Example 2:
```
Input: candidates = [1], target = 3
Output: [[1, 1, 1]]
```
### Notice
1. All numbers (including target) will be positive integers.
2. Numbers in a combination `a1, a2, … , ak` must be in non-descending order. (ie, `a1 ≤ a2 ≤ … ≤ ak`)
3. Different combinations can be in any order.
4. The solution set must not contain duplicate combinations.