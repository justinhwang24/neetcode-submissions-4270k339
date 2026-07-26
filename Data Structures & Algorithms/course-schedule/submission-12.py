class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            prereqs[a].append(b)
        
        visiting = set()
        def dfs(cur):
            if cur in visiting:
                return False
            if not prereqs[cur]:
                return True
            visiting.add(cur)
            for pre in prereqs[cur]:
                if not dfs(pre):
                    return False
            visiting.remove(cur)
            prereqs[cur] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True