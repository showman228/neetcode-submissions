class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def bfs(row: int, col: int) -> int:
            q = deque()
            grid[row][col] = 0
            cnt = 1
            q.append((row, col))

            while q:
                row, col = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc

                    if not (0 <= nr < ROWS and 0 <= nc < COLS) or grid[nr][nc] == 0:
                        continue
                    
                    q.append((nr, nc))
                    cnt += 1
                    grid[nr][nc] = 0
            
            return cnt

        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res