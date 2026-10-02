class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        res = 0
        dct = dict()
        for right in range(len(s)):
            if s[right] not in dct:
                dct[s[right]] = dct.get(s[right], 0) + 1
                res = max(res, len(dct))
            else:
                left = right
                dct.clear()


        return res