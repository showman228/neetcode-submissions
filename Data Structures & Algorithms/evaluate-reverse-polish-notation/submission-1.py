class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in "+-*/" and len(stack) >= 2:
                first = int(stack.pop())
                second = int(stack.pop())
                
                if c == '-':
                    stack.append(first - second)
                elif c == '+':
                    stack.append(first + second)
                elif c == '*':
                    stack.append(first * second)
                elif c == '/':
                    stack.append(first / second)
            
            elif c.isdigit():
                stack.append(c)
            
        return stack[-1]
