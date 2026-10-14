class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sp = [[] for _ in range(len(nums) + 1)]
        count = dict()

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, cnt in count.items():
            sp[cnt].append(num)


        res = []
        for i in range(len(sp) - 1, -1, -1):
            if k == 0:
                break

            for num in sp[i]:
                res.append(num)
                k -= 1

        return res