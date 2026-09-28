class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        for i in range(len(res)):
            for j in range(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res[i] = j - i
                    break


        return res 
