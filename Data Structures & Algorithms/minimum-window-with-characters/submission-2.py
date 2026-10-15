class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        dct_t = dict()

        for char in t:
            dct_t[char] = dct_t.get(char, 0) + 1

        left = 0

        have, need = 0, len(t)

        res, resLen = [-1, -1], float("inf")
        dct_s = dict()
        for right in range(len(s)):
            dct_s[s[right]] = dct_s.get(s[right], 0) + 1
            
            if s[right] in dct_t and dct_s[s[right]] == dct_t[s[right]]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                dct_s[s[left]] -= 1
                if s[left] in dct_t and dct_s[s[left]] < dct_t[s[left]]:
                    have -= 1
                
                left += 1

        left, right = res
        return s[left:right + 1] if resLen != float("inf") else ""