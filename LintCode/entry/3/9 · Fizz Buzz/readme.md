# Description
Given number `n`. Print number from 1 to n. According to following rules:

- when number is divided by `3`, print `"fizz"`.
- when number is divided by `5`, print `"buzz"`.
- when number is divided by both `3` and `5`, print `"fizz buzz"`.
- when number can't be divided by either `3` or `5`, print the number itself.
# Example
```
If n = 15, you should return:
[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]

If n = 10, you should return:
[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz"
]
```
# Challenge
Can you do it with only one `if` statement?