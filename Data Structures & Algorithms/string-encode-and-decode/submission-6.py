class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        res = ""
        for elem in strs:
            res += str(len(elem)) + "$" + elem
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
    
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "$":
                j += 1

            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            
            i = j

        return res




            
