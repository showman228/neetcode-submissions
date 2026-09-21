class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dct1 = dict()
        dct2 = dict()

        for i in range(len(s)):
            dct1[s[i]] = dct1.get(s[i], 0) + 1
            dct2[t[i]] = dct2.get(t[i], 0) + 1
        
        return dct1 == dct2