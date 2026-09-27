class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for char in tokens:
            if char in "+-*/":
                if char == '+':
                    stack.append(stack.pop() + stack.pop())
                elif char == '*':
                    stack.append(stack.pop() * stack.pop())
                elif char == "/":
                    value1, value2 = stack.pop(), stack.pop()
                    stack.append(int(float(value2) / value1))
                elif char == "-":
                    value1, value2 = stack.pop(), stack.pop()
                    stack.append(value2 - value1)
            else:
                stack.append(int(char))

        return stack[0]