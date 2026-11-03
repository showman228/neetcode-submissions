class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
                    q.append((r, c))
        
        while q:
            row, col = q.popleft()
            if board[row][col] == "O":
                board[row][col] = "T" # safe zone
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS - 1 and 0 <= nc < COLS - 1) and board[nr][nc] == "O":
                        q.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        


            
