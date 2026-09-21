class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sp = [[] for _ in range(len(nums) + 1)]

        dct = dict()
        for num in nums:
            dct[num] = dct.get(num, 0) + 1

        for num, count in dct.items():
            sp[count].append(num)

        res = []
        for i in range(len(sp) - 1, -1, -1):
            if k == 0:
                break

            for c in sp[i]:
                res.append(c)
                k -= 1
        
        return res
        