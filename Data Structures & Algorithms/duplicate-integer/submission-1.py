class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = dict()
        for elem in nums:
            dct[elem] = dct.get(elem, 0) + 1
        for count in dct.values():
            if count != 1:
                return True
        
        return False