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
        last_step = 0
        while left <= right:
            if self.isPalindrom(s, left, right):
                return s[left:right + 1]
            if last_step == 0:
                left += 1
                last_step = 1
            elif last_step == 1:
                right -= 1
                last_step = 0
        return s[0]