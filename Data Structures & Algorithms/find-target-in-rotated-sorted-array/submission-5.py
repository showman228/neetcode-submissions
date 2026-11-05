class Solution:
    def BS(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        res = self.BS(nums, 0, left - 1, target)
        if res != -1:
            return res

        return self.BS(nums, left, right, target)
        