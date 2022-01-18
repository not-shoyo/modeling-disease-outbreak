class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q, ans, n = [], [], len(graph)
        q.append([0])
        while len(q) != 0:
            path = q.pop(0)
            if path[-1] == n - 1:
                ans.append(path)
            else:
                for nextNode in graph[path[-1]]:
                    pCopy = path.copy()
                    pCopy.append(nextNode)
                    q.append(pCopy)
        return ans
            
