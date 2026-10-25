class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(row: int, col: int) -> int:
            
            if not (0 <= row < ROWS and 0 <= col < COLS) or (row, col) in visit or grid[row][col] == 0:
                return 0

            visit.add((row, col))
            return (1 + dfs(row + 1, col) +
                        dfs(row - 1, col) + 
                        dfs(row, col + 1) +
                        dfs(row, col - 1))

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res