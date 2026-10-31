class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i, x in enumerate(nums):
            if target - x in hs:
                return [hs[target-x], i]
            hs[x] = i
        
        return [-1, -1]