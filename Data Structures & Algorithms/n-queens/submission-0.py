class Solution:
    def isValidPlace(self, r, c, board) -> bool:
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        
        row = r - 1
        col = c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        row = r - 1
        col = c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        solution = []

        def dfs(row):

            if row == n:
                copy = ["".join(r) for r in board]
                solution.append(copy)
                return

            for col in range(n):
                if self.isValidPlace(row, col, board):
                    board[row][col] = "Q"
                    dfs(row + 1)
                    board[row][col] = "."

        dfs(0)
        return solution