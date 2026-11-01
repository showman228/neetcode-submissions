class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)

        prefix_sum = 0
        for i, num in enumerate(nums):

            if prefix_sum == sum_nums - prefix_sum - num:
                return i

            prefix_sum += num

        return -1