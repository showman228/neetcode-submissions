class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        hs = Counter(s)
        max_effort = max(hs.values())
        for right in range(len(s)):
            while (right - left + 1) - max_effort > k:
                left += 1
                res -= 1
            res = max(res, right - left + 1)
        
        return res