class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preHash = { i:[] for i in range(numCourses)}

        for i, edge in prerequisites:
            preHash[i].append(edge)

        visit = set()
        def dfs(i: int):
            
            if i in visit:
                return False

            if preHash[i] == []:
                return True

            visit.add(i)
            for pre in preHash[i]:
                if not dfs(pre): return False

            visit.remove(i)
            preHash[i] = []

            return True

        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True