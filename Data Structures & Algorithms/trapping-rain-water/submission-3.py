class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 
        
        stack = []
        counter_water = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - mid
                    w = i - stack[-1] - 1
                    counter_water += h * w
                
            stack.append(i)
        
        return counter_water