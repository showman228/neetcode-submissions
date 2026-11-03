class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row: int, col: int):
            
            if not (0 < row < ROWS - 1 and 0 < col < COLS - 1) or board[row][col] == "X":
                return 

            board[row][col] = "X"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    dfs(r, c)
    