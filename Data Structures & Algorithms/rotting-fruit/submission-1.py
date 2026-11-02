class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        minute = 0
        fresh = 0


            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()
                for dr, dc in ((1,0), (0,1), (-1, 0), (0, -1)):
                    nr, nc = row + dr, col + dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
                
            minute += 1


        return minute if fresh == 0 else -1