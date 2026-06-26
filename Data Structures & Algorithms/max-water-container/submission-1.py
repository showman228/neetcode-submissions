class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_square = float("-inf")
        while left < right:
            min_height = min(heights[left], heights[right])

            square = (right - left) * min_height

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

            max_square = max(max_square, square)

        
        return max_square