class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dct = dict()

        for elem in nums:
            if elem in dct:
                return elem
            dct[elem] = dct.get(elem, 0) + 1
        
        return -1