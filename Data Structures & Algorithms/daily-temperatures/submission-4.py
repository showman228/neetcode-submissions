class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = len(temperatures)
                    break
                j += res[j]
            
            if j < len(temperatures):
                res[i] = j - i
        
        return res