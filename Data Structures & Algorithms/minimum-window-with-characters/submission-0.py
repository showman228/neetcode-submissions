class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t) or t == "":
            return ""
        
        countS, countT = dict(), dict()

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")

        left = 0
        for right in range(len(s)):
            countS[s[right]] = countS.get(s[right], 0) + 1

            if s[right] in countT and countS[s[right]] == countT[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                countS[s[left]] -= 1
                if s[left] in countT and countS[s[left]] < countT[s[left]]:
                    have -= 1
                
                left += 1
            

        left, right = res

        return s[left:right+1] if resLen != float("inf") else ""