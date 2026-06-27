class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in "+-*/":
                second = stack.pop()
                first = stack.pop()
    
                if c == '-':
                    stack.append(first - second)
                elif c == '+':
                    stack.append(first + second)
                elif c == '*':
                    stack.append(first * second)
                elif c == '/':
                    stack.append(int(first / second))
            
            else:
                stack.append(int(c))
            
        return stack[-1]
