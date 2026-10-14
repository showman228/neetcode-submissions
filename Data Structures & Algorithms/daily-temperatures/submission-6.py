class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res: List[int] = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res