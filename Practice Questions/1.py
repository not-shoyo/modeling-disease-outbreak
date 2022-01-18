from queue import Queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = Queue(maxsize = m*n)
        fresh = 0
        time = 0
        
        # print(m, n, q.qsize(), fresh, time)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.put((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        # print (q.qsize(), fresh)
        
        while not q.empty():
            rottenOranges = q.qsize()
            for i in range(rottenOranges):
                pair = q.get()
                x = pair[0]
                y = pair[1]
                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    fresh -= 1
                    q.put((x-1, y))
                    print((x-1, y))
                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    fresh -= 1
                    q.put((x, y-1))
                    print((x, y-1))
                if x < m-1 and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    fresh -= 1
                    q.put((x+1, y))
                    print((x+1, y))
                if y < n-1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    fresh -= 1
                    q.put((x, y+1))
                    print((x, y+1))
            if not q.empty():
                time += 1
        
        return time if fresh == 0 else -1
