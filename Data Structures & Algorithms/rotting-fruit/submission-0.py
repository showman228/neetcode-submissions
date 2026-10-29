class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        minute = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()

                for dr, dc in ((1, 0), (0, 1), (0, -1), (-1, 0)):
                    nr, nc = row + dr, col + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr, nc])
                        fresh -= 1

            minute += 1

        return minute if fresh == 0 else -1        