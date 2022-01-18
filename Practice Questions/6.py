class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        mapping = [[] for x in range(n)]
        visited = [-1 for x in range(n)]
        count, edges = 0, len(connections)
        
        for connection in connections:
            mapping[connection[0]].append(connection[1])
            mapping[connection[1]].append(connection[0])

        
        # print(mapping)
        
        def dfs(node):
            visited[node] = 0
            for connected in mapping[node]:
                if visited[connected] == -1:
                    dfs(connected)
                
        for i in range(n):
            if visited[i] == -1:
                count += 1
                dfs(i)
        
        # print(edges, n, count)
        
        extra = edges - (n - 1) + (count - 1)
        
        if extra >= count - 1:
            return count - 1
        else:
            return -1
