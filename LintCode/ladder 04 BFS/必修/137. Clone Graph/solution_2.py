# BFS without sub-functions: https://www.lintcode.com/problem/137/?_from=ladder&fromId=161

"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return node

        # 将题目给定的节点添加到队列
        queue = [node]
        # 克隆第一个节点并存储到哈希表中
        clone = UndirectedGraphNode(node.label)
        visited = {node:clone}

        while queue:
            # 取出队列的头节点
            new = queue.pop(0)
            # 遍历该节点的邻居
            for n in new.neighbors:
                if n not in visited:
                    # 如果没有被访问过，就克隆并存储在哈希表中
                    visited[n] = UndirectedGraphNode(n.label)
                    # 将邻居节点加入队列中
                    queue.append(n)
                # 更新当前节点的邻居列表
                visited[new].neighbors.append(visited[n])

        return clone