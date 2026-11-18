class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suffix = 0
        prefix = 0
        res = nums[0]
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums) - i - 1] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res