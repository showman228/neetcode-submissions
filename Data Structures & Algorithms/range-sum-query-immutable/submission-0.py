class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum: List[int] = [0]
        for i in range(len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])
        
        self.prefix_sum = self.prefix_sum[1:]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]

        return self.prefix_sum[right] - self.prefix_sum[left - 1]      


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)