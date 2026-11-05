class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left


        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                
            return -1

        res = binary_search(0, pivot - 1)
        if res != -1:
            return res

        return binary_search(pivot, len(nums) - 1)
        

        