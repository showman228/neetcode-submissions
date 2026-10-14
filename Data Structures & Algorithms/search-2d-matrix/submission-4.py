class Solution:
    def binarySearch(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if target in matrix[mid]:
                return self.binarySearch(matrix[mid], target)
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False