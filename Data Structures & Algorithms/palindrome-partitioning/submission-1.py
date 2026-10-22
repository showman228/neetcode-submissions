class Solution:
    def palindrom(self, s: str, l: int, r: int) -> bool:
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(path, i):

            if i == len(s):
                res.append(path[:])
                return
            
            if i >= len(s):
                return

            for j in range(i, len(s)):
                if self.palindrom(s, i, j):
                    path.append(s[i: j + 1])
                    dfs(path, j + 1)
                    path.pop()

        dfs([], 0)
        return res
                
