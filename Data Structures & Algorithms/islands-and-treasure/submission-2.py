class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def bfs(r: int, c: int):
            visit = set()
            q = deque([(r, c)])
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        nr, nc = row + dr, col + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS) and grid[nr][nc] != -1 and (nr, nc) not in visit:
                            
                            q.append((nr, nc))
                            visit.add((row, col))
                steps += 1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
