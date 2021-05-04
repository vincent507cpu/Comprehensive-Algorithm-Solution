# Description
Six degrees of separation is a philosophical problem, which means that everyone and everything can be connected through six steps or less.

Now give you a friendship, calculate how many steps two people can be connected through, if not, return `-1`.

# Example
## Example1
```
Input: {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4 
Output: 2
Explanation:
    1------2-----4
     \          /
      \        /
       \--3--/
```
## Example2
```
Input: {1#2,4#3,4#4,2,3} and s = 1, t = 4
Output: -1
Explanation:
    1      2-----4
                 /
               /
              3
```