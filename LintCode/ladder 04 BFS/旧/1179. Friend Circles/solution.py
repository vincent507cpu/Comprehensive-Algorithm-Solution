class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        n = len(M) # 人数
        res = 0 # 答案
        visited = [False for _ in range(n)] # 标记是否访问过
        
        for i in range(n): # 遍历每个人，如果这个人还没访问过 就从这个人开始做一遍bfs
            if not visited[i]:
                res += 1
                visited[i] = True
                queue = [i] # 标记起点并压入队列
                
                while queue:
                    now = queue.pop(0) # 取出队首
                    
                    for j in range(n): # 从队首找朋友
                        if M[now][j] == 1 and not visited[j]: # 找到新朋友（之前没访问过的朋友）就标记访问并压入队列
                            visited[j] = True
                            queue.append(j)
                            
        return res