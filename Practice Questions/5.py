class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited, n = [], len(isConnected)
        for j in range(n):
            visited.append(-1)
            
        def dfs(i):
            if visited[i] == 0:
                return
            visited[i] = 0
            for j in range(n):
                if isConnected[i][j] == 1 and visited[j] == -1:
                    dfs(j)
        
        count = 0
        for i in range(n):
            if (1 in isConnected[i]) and visited[i] == -1:
                count += 1
                dfs(i)
                # print("In If Block")
        
        return count
