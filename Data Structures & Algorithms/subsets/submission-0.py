class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        state = []

        def backtraking(i):

            if i == len(nums):
                res.append(state.copy())
                return
            
            state.append(nums[i])
            backtraking(i + 1)

            state.pop()
            backtraking(i + 1)
        
        backtraking(0)
        return res