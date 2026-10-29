class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        def addCell(row: int, col: int):
            if not (0 <= row < ROWS and 0 <= col < COLS) or grid[row][col] == -1 or (row, col) in visit:
                return

            visit.add((row, col))
            q.append([row, col]) 
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            lentgh = len(q)
            for i in range(lentgh):
                row, col = q.popleft()
                grid[row][col] = dist
                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)
            dist += 1
        
