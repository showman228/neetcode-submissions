class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            cnt = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nc < 0 or nr < 0 or nc >= cols or nr >= rows or grid[nr][nc] == 0):
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    cnt += 1

            return cnt

            
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        
        return res