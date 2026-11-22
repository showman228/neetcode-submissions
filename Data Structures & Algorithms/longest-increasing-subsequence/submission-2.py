class Solution:
    def binarySearch(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minf = float("inf")
        while left <= right:
            mid = (left + right) // 2


    def lengthOfLIS(self, nums: List[int]) -> int:
        count = 1
        idx = nums.index(min(nums))
        for i in range(idx, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
        return count