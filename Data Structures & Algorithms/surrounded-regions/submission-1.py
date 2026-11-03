class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        q = deque()

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == "O":
                    q.append((r, c))

        while q:
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()

                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nr, nc = row + dr, col + dc

                    if (0 < nr < ROWS - 1 and 0 < nc < COLS - 1) and board[nr][nc] == "O":
                        board[nr][nc] = "X"
                        q.append((nr, nc))
            
