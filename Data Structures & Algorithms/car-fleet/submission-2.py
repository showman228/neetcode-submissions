class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_speed = [(position[i], speed[i]) for i in range(len(position))]

        stack = []
        for p, s in sorted(pos_speed)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)