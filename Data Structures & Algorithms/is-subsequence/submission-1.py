class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p_s = 0
        p_t = 0
        while p_t < len(t) and p_s < len(s):
            
            if s[p_s] != t[p_t]:
                p_t += 1
            else:
                p_s += 1
                p_t += 1
        
        return p_s == len(s)
