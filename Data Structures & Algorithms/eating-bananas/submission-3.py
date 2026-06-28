class Solution:
    def test_speed(self, nums: List[int], k: int, h: int) -> int:

        for num in nums:
            h -= math.ceil(num / k)
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r

        while l <= r:
            mid = (l + r) // 2
            
            if self.test_speed(piles, mid, h) >= 0:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        
        return result 
            




