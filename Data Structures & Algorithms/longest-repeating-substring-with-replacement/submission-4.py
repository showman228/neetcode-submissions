class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct = dict()
        res = 0

        left = 0
        maxf = 0
        for right in range(len(s)):

            dct[s[right]] = dct.get(s[right], 0) + 1
            maxf = max(maxf, dct[s[right]])

            while (right - left + 1) - maxf > k:
                dct[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        
        return res
