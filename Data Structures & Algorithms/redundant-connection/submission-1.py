class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]
        for cur, nei in edges:
            adj[cur].append(nei)
            adj[nei].append(cur)


        visit = [False] * (len(edges) + 1)
        cycle = set()
        cycleStart = -1


        def dfs(node, par):
            nonlocal cycleStart
            if visit[node]:
                cycleStart = node
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart -= 1
                    return True
            return False

        dfs(1, -1)

        for cur, nei in reversed(edges):
            if cur in cycle and nei in cycle:
                return [cur, nei]
        return []

        
        