class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sp = [0] * (len(nums) + 1)
        for num in nums:
            if num in sp:
                continue
            else:
                sp[nums.count(num)] = num #idx -> кол-во чисел; value -> самое значение

        res = []
        for i in range(len(sp) - 1, -1, -1):
            if k == 0:
                break

            if sp[i] != 0:
                res.append(sp[i])
                k -= 1
        
        return res
        