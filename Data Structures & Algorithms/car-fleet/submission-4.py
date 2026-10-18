class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        pos_speed = [[pos, speed] for pos, speed in zip(position, speed)]

        pos_speed.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for p, s in pos_speed:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
            
        return len(stack)