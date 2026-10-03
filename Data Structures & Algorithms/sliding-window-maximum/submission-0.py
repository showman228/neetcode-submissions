class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0

        max_elem_window = float("inf")
        res = []
        for right in range(len(nums)):
            while (right - left + 1) >= k:
                max_elem_window = max(nums[left:right + 1])
                res.append(max_elem_window)
                left += 1
        
        return res