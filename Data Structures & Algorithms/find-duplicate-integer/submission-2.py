class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            lessOrEqual = sum(1 for num in nums if num <= m)

            if lessOrEqual <= m:
                l = m + 1
            else:
                r = m

        return l