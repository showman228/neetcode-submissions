class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1:
            return False

        adj = [[] for _ in range(n)]

        for cur, nei in edges:
            adj[cur].append(nei)
            adj[nei].append(cur)

        q = deque()
        q.append((0, -1))
        visit = set()
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                
                visit.add(nei)
                q.append((nei, node))
        
        return len(adj) == n

        
