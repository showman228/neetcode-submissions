class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            min_value = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    min_value = j - i
                    break
            res.append(min_value)
        
        return res