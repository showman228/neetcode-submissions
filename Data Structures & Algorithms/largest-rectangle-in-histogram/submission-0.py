class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_square = 0

        stack = [] # будем хранить индексы и высоту (idx, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_square = max(max_square, (i - index) * height)
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_square = max(max_square, h * (len(heights) - i))



        return max_square