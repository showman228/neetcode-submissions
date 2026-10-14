class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        countOfWater = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                countOfWater += (leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                countOfWater += (rightMax - height[right])
    
        return countOfWater
        
