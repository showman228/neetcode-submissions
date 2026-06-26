class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        for i in range(len(nums)):

            if (i > 0 and nums[i] == nums[i - 1]):
                continue

            left = i + 1
            right = len(nums) - 1
            total = 0

            while left < right:
                total = nums[left] + nums[i] + nums[right]

                if (total == 0):
                    temp = [nums[left], nums[i], nums[right]]
                    res.append(temp)
                    left += 1

                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1
                
                elif (total > 0):
                    right -= 1
                
                elif (total < 0):
                    left += 1
            
        return res
                    

