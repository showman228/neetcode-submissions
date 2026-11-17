class Solution:
    def dfs(self, sp, nums, visit, res) -> None:
        
        if len(sp) == len(nums):
            res.append(sp.copy())
            return

        for i in range(len(nums)):
            if not visit[i]:
                sp.append(nums[i])
                visit[i] = True
                self.dfs(sp, nums, visit, res)
                sp.remove(nums[i])
                visit[i] = False


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = [False] * len(nums)
        sp = []
        self.dfs(sp, nums, visit, res)
        return res
    
    
    

        

        