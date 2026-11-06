class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        cnt = 0

        for cur, nei in edges:
            adj[cur].append(nei)
            adj[nei].append(cur)
            
        def dfs(i):        
            for nei in adj[i]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

            

        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                cnt += 1
        
        return cnt