class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, alt = set(), set()

        def dfs(row: int, col, visit: set, prevHeight: int):
            if not (0 <= row < ROWS and 0 <= col < COLS) or (row,col) in visit or heights[row][col] < prevHeight:
                return

            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS - 1, alt, heights[row][COLS - 1])

        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, alt, heights[ROWS - 1][col])

        solution = [] # [row, col]
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in alt:
                    solution.append([r, c])
        return solution