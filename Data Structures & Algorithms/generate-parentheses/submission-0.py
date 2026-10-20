class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(path, left, right):
            
            if left == right == n:
                res.append("".join(path))
                return 

            if left > right:
                path.append(")")
                dfs(path, left, right + 1)
                path.pop()

            if left < n:
                path.append("(")
                dfs(path, left + 1, right)
                path.pop()

        dfs([], 0, 0)
        return res
