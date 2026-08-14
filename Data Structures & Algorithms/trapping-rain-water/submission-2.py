class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        counter_water = 0
        while left < right:
            if (leftMax < rightMax):
                left += 1
                leftMax = max(leftMax, height[left])
                counter_water += (leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                counter_water += (rightMax - height[right])
        
        return counter_water