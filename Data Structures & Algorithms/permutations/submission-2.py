class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = [False] * len(nums)
        sp = []

        def dfs():
            if len(sp) == len(nums):
                res.append(sp.copy())
                return

            for i in range(len(nums)):
                if not visit[i]:
                    sp.append(nums[i])
                    visit[i] = True
                    dfs()
                    sp.pop()
                    visit[i] = False
        dfs()
        return res
    
    
    

        

        