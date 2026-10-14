class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sp = [[] for _ in range(len(nums))]
        res = []

        # заполнить sp
        for num in nums:
            cnt = nums.count(num)
            if num not in sp[cnt - 1]:
                sp[cnt - 1].append(num)

        # идем в обратно направлении sp и добавляем значение/я в res
        for i in range(len(sp) - 1, -1, -1):
            if sp[i]:
                res.extend(sp[i])
                k -= 1
            if k == 0:
                break

        return res

        