class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = []
        hashMap = {i:[] for i in range(numCourses)}
        for preReq in prerequisites:
            hashMap[preReq[0]].append(preReq[1])
        
        # print(hashMap)
        
        def dfs(course):
            if course in visited:
                return False
            if hashMap[course] == []:
                return True
            
            visited.append(course)
            
            for reqs in hashMap[course]:
                res = dfs(reqs)
                if not res:
                    return False
                hashMap[course].remove(reqs)
            visited.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
