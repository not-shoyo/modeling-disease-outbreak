class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        nConnections = len(connections)
        reach, low = [-1 for i in range(n)], [-1 for i in range(n)]
        critical, visited, adj = [], [-1 for i in range(n)], [[] for i in range(n)]
        for connection in connections:
            adj[connection[0]].append(connection[1])
            adj[connection[1]].append(connection[0])
        
        # print(adj)
        
        self.timer = 0
        
        def dfs(node: int, parent: int):
            # print("In dfs with " , node , " and " , parent, timer[0])
            # print(node)
            visited[node] = 0
            reach[node] = low[node] = self.timer
            self.timer += 1

            for child in adj[node]:
                if child == parent:
                    continue
                if visited[child] == -1:
                    dfs(child, node)
                    low[node] = min(low[node], low[child])
                    if low[child] > reach[node]:
                        critical.append([node, child])
                elif child != parent:
                    low[node] = min(low[node], reach[child])
        
        for i in range(n):
            if visited[i] == -1:
                print(i)
                dfs(i, -1)
        
        return critical
