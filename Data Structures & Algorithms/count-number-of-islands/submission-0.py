class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            if not(0 <= r < rows and 0 <= c < cols) or grid[r][c] != '1':
                return 
            grid[r][c] = "0"
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                dfs(r + dr, c + dc)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)

        return count