class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
                
        if len(digits) == 0:
            return []

        dct = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        q = deque()
        q.append("")

        while q and len(q[0]) < len(digits):
            prefix = q.popleft()
            digit = digits[len(prefix)]

            for letter in dct[digit]:
                q.append(prefix + letter)
        
        return list(q)

