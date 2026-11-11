class Solution:
    def isPalindrom(self, s, l: int, r: int) -> bool:
        left = l
        right = r 
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True


    def longestPalindrome(self, s: str) -> str:
        res = []
        def dfs(left: int, right: int):
            if left == right:
                return False
            if self.isPalindrom(s, left, right):
                res.append(s[left:right + 1])
                return True

            return (dfs(left + 1, right) or dfs(left, right - 1))
        
        dfs(0, len(s) - 1)

        return max(res, key=lambda x: len(x))

