class Solution:
    def searchBorder(self, nums: List[int]) -> Tuple(int):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            
        
        return (left, right)

    def search(self, nums: List[int], target: int) -> int:
        right, left = self.searchBorder(nums)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return -1