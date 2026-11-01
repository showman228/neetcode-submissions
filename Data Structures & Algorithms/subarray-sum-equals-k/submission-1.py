class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0

        prefix_sum = {0:1} # prefix_sum: count

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefix_sum.get(diff, 0)
            prefix_sum[curSum] = prefix_sum.get(curSum, 0) + 1
        
        return res