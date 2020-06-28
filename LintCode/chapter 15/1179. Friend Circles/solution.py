class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        res, queue = 0, []
        visited = [False for _ in range(len(M))]
        
        for i in range(len(M)):
            if not visited[i]:
                res += 1
                visited[i] = True
                queue.append(i)
                
                while queue:
                    node = queue.pop(0)
                    
                    for j in range(len(M)):
                        if M[node][j] and not visited[j]:
                            visited[j] = True
                            queue.append(j)
                            
        return res