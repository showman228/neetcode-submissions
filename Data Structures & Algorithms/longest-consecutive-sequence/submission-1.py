class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        nums = sorted(nums)

        max_len = 0
        cnt = 1
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                cnt += 1
            else:
                cnt = 1

            max_len = max(max_len, cnt)

        return max_len + 1

