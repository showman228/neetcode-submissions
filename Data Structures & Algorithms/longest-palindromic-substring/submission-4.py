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
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1
        
        return s[resIdx : resIdx + resLen]


