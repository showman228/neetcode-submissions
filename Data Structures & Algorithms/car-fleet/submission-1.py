class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_speed = [(position[i], speed[i]) for i in range(len(position))]
        sorted(pos_speed, key=lambda x: x[0], reverse=True)

        stack = []
        for p, s in pos_speed:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)