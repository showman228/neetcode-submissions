class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = dict() # index: target - value

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dct:
                return [dct[diff], i]
            
            dct[n] = i

        return [-1, -1]