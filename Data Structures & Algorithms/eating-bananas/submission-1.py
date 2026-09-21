class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def canFinish(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += pile // k
                if pile % k != 0:
                    hours += 1
                if hours > h:
                    return False
            return True
        

        ans = right
        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans