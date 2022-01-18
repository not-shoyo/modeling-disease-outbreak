class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        arr = []
        for i in range(m):
            arr.append([])
            for j in range(n):
                arr[i].append(-1)
        count = 0
        
        def dfs(i, j, arr):
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return
            if grid[i][j] == "0" or arr[i][j] == 0:
                return
            arr[i][j] = 0
            # print(i, j, arr)
            dfs(i-1, j, arr)
            dfs(i+1, j, arr)
            dfs(i, j-1, arr)
            dfs(i, j+1, arr)
                    
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if arr[i][j] == -1:
                        count += 1
                        dfs(i, j, arr)
                    # print(count)
                    # print(arr)
        
        return count
