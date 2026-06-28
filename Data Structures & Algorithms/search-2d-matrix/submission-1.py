class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)- 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.binarySearch(matrix[mid], target)
            else:
                if matrix[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return False