class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right -= 1
            else:
                left += 1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left < right:
            mid = (left + right) // 2
            if target in matrix[mid]:
                return self.binarySearch(matrix[mid], target)
            elif matrix[mid][-1] < target:
                left += 1
            else:
                right -= 1
        
        return False