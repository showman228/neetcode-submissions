class MinStack:

    def __init__(self):
        self.min_value = float("inf")
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_value = val
        else:
            self.stack.append(val - self.min_value)
            if val < self.min_value:
                self.min_value = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min_value -= pop


    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min_value
        else:
            return self.min_value

    def getMin(self) -> int:
        return self.min_value
        
