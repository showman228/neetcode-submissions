class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
    
        dct = dict()
        for elem in s:
            dct[elem] = dct.get(elem, 0) + 1
    
        dct = sorted(dct.items(), key=lambda item: item[1])

        highest_value_encountered = dct[1][0]
        less_value_encountered = dct[0][0]
        
        l = 0
        max_len = 0
        cnt = 0
        s = s.replace(less_value_encountered, highest_value_encountered, k)
        for r in range(len(s)):
            if s[r] == less_value_encountered:
                l = r + 1
                cnt = 0
            else:
                cnt += 1
        
            max_len = max(max_len, cnt)
    
        return max_len
            
        

        


