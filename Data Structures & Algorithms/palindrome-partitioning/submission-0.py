class Solution:
    def palindrom(self, s: str, l: int, r: int) -> bool:
        left = l
        right = r

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def dfs(path: List[str], i: int):

            if i >= len(s):
                res.append(path[:])
            
            for j in range(i, len(s)):
                if self.palindrom(s, i, j):
                    path.append(s[i: j + 1 ])
                    dfs(path, j + 1)
                    path.pop()

        dfs([], 0)
        return res
            