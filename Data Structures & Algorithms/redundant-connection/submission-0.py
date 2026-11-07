class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]
        indegree = [0] * (len(edges) + 1)
        for cur, nei in edges:
            adj[cur].append(nei)
            adj[nei].append(cur)
            indegree[cur] += 1
            indegree[nei] += 1
        
        q = deque([i for i in range(1, len(edges) + 1) if indegree[i] == 1])

        while q:
            node = q.popleft()
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    q.append(nei)
        
        for cur, nei in reversed(edges):
            if indegree[cur] == 2 and indegree[nei]:
                return [cur, nei]
        return []


        
        