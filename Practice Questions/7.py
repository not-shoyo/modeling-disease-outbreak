class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        redundantConnections, n = [], len(edges)
        unionFindList = [i for i in range(n)]
        heightList = [1 for i in range(n)]
        
        def root(a: int):
            i = unionFindList[a]
            while unionFindList[i] != i:
                i = unionFindList[unionFindList[i]]
            return i
        
        def union(a: int, b: int):
            rootA, rootB = root(a), root(b)
            heightA, heightB = heightList[rootA], heightList[rootB]
            if heightA > heightB:
                unionFindList[rootB] = rootA
                heightA += heightB
            else:
                unionFindList[rootA] = rootB
                heightB += heightA
        
        for edge in edges:
            if root(edge[0]-1) == root(edge[1]-1):
                redundantConnections.append(edge)
            else:
                union(edge[0]-1, edge[1]-1)
        
        return redundantConnections[-1]
            
