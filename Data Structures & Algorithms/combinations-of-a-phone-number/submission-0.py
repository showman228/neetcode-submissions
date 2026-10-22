class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
                
        if len(digits) == 0:
            return []

        dct = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        def dfs(curStr: str, i: int):

            if len(curStr) == len(digits):
                res.append(curStr)
                return 

            for char in dct[digits[i]]:
                dfs(curStr + char, i + 1)

        dfs("", 0)
        return res