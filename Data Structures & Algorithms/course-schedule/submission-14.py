class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            prereqs[a].append(b)
        
        visit = set()

        def dfs(cur):
            if cur in visit:
                return False
            if not prereqs[cur]:
                return True
            visit.add(cur)
            for child in prereqs[cur]:
                if not dfs(child):
                    return False
            visit.remove(cur)
            prereqs[cur] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        