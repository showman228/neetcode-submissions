class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        l, r = 0, 1

        best_len = 1
        while r < len(s):
        
            if s[r] in s[l:r]:
                best_len = max(best_len, len(s[l:r]))
                l = r

            r += 1

        return best_len