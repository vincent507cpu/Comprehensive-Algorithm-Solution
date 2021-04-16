"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""

'''
这是一个非常通用的利用 stack 进行 Binary Tree Iterator 的写法。

stack 中保存一路走到当前节点的所有节点，stack.peek() 一直指向 iterator 指向的当前节点。 因此判断有没有下一个，只需要判断 stack 是否为空 获得下一个值，只需要返回 stack.peek() 的值，并将 stack 进行相应的变化，挪到下一个点。

挪到下一个点的算法如下：

  1. 如果当前点存在右子树，那么就是右子树中“一路向西”最左边的那个点
  2. 如果当前点不存在右子树，则是走到当前点的路径中，第一个左拐的点
  
访问所有节点用时O(n)，所以均摊下来访问每个节点的时间复杂度时O(1)
'''

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        self.cur = root
        
    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return bool(self.cur) or len(self.stack) > 0
        
    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
            
        self.cur = self.stack.pop()
        nxt = self.cur
        self.cur = self.cur.right
        return nxt