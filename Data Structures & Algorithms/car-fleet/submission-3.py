class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: 
        pos_speed = [[pos, speed] for pos, speed in zip(position, speed)]

        pos_speed.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for p, s in pos_speed:
            time = (target - p) / s
            if stack and time <= stack[-1]:
                stack.pop()
            stack.append(time)
            
        return len(stack)