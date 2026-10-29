class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(row: int, col: int):
            
            if not (0 <= row < ROWS and 0 <= col < COLS) or grid[row][col] == -1 or visit[row][col]:
                return INF

            if grid[row][col] == 0:
                return 0
            
            visit[row][col] = True
            res = INF
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                res = min(res, 1 + dfs(row + dr, col + dc))
            visit[row][col] = False
            return res
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r, c)
