class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        res = 0
        dct = dict()
        for right in range(len(s)):
            while s[right] in dct.keys():
                dct.pop(s[left])
                left += 1

            dct[s[right]] = dct.get(s[right], 0) + 1
            res = max(res, len(dct))
                
        return res