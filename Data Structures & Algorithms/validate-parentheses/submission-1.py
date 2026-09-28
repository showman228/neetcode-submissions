class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            "(": ")",
            "{": "}",
            "[": "]",
            "<": ">"
        }

        stack = []
        for char in s:
            if char in ")}]>":
                if stack and dct[stack.pop()] == char:
                    continue
                else:
                    return False
            else:
                stack.append(char)
        
        return True