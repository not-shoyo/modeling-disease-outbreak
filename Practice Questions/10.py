class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        queue = []
        m, n = len(grid), len(grid[0])
        
        def find(check : int):
            numOfIslands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == check:
                        numOfIslands += 1
                        queue.append((i,j))

                        while len(queue) > 0:
                            a, b = queue.pop(0)
                            if grid[a][b] == check:
                                grid[a][b] = -check
                                for direction in directions:
                                    newI, newJ = a + direction[0], b + direction[1]
                                    if 0 <= newI < m and 0 <= newJ < n:
                                        if grid[newI][newJ] == check:
                                            queue.append((newI, newJ))
            
            return numOfIslands
                            
        p = 1
        if find(p) > 1:
            return 0
        p = -p
        for i in range(m):
            for j in range(n):
                if grid[i][j] == p:
                    grid[i][j] = 0
                    if find(p) != 1:
                        # print(i, j, find(p))
                        return 1
                    grid[i][j] = -p
                    p = -p

        return 2
