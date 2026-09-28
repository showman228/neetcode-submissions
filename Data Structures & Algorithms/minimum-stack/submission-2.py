class MinStack:

    def __init__(self):
        self.min_val = float("inf")
        self.stack = []

    def push(self, val: int):
        self.stack.append(val)

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return min(self.stack)
