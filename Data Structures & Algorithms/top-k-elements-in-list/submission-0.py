class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        freq_list = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, val in count.items():
            freq_list[val].append(num)

        res = []
        
        for i in range(len(freq_list) - 1, 0, -1):
            for c in freq_list[i]:
                res.append(c)
                k -= 1
            if k == 0:
                break
        return res
                


