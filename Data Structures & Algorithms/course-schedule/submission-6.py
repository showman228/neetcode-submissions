class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for cur, nei in prerequisites:
            adj[cur].append(nei)
        
        visit = set()

        def dfs(node: int):
            
            if node in visit:
                return False

            if adj[node] == []:
                return True
            
            visit.add(node)

            for nei in adj[node]:
                if not dfs(nei): return False

            visit.remove(node)
            adj[node] = []
        
            return True
            
        for cur in range(numCourses):
            if not dfs(cur): return False
        
        return True

            