class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        hs = {}
        maxf = 0
        for right in range(len(s)):
            hs[s[right]] = 1 + hs.get(s[right], 0)
            maxf = max(maxf, hs[s[right]])
            while (right - left + 1) - maxf > k:
                hs[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res