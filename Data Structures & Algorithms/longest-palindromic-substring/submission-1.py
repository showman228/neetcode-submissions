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
        left = 0
        right = len(s) - 1
        while left <= right:
            if self.isPalindrom(s, left, right):
                return s[left:right + 1]
            left += 1
            right -= 1
        return s[0]