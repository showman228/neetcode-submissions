class Solution:
    def isValid(self, s: str) -> bool:
        dct = {
            ")": "(",
            "}": "{",
            "]": "[",
            ">": "<"
        }

        stack = []
        for char in s:
            if char in ")}]>":
                if stack and stack[-1] == dct[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False