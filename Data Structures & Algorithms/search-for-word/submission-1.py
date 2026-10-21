class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row: int, col: int, i: int):
            
            if i == len(word):
                return True
            
            if not (0 <= row < ROWS and 0 <= col < COLS) or board[row][col] == "#" or board[row][col] != word[i]:
                return False
            

            board[row][col] = "#"
            res = (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1)
            )
            board[row][col] = word[i]
            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False