class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        res = ""
        for elem in strs:
            res += elem + "$"
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
    
        res = []
        i = 0
        while i < len(s):

            inx = s.find("$", i)
            res.append(s[i:inx])
            i = inx + 1

        return res




            
