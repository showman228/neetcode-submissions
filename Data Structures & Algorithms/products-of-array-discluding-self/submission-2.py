class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_count = 0

        for elem in nums:
            if elem == 0:
                zero_count += 1
            else:
                total_prod *= elem

        
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i in range(len(nums)):

            if zero_count > 0:
                if nums[i] == 0:
                    res[i] = total_prod
                else:
                    res[i] = 0
                
            else:
                res[i] = total_prod//nums[i]
        
        return res
