class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [(0,-1)]

        max_rectangle = 0
        for i, height in enumerate(heights):
            while len(stack) > 1 and stack[-1][0] > height:
                bar_height, bar_idx = stack.pop()
                width = i - stack[-1][1] - 1
                rectangle = bar_height*width
                max_rectangle = max(max_rectangle, rectangle)

            stack.append((height, i))
        
        while len(stack) > 1:
            bar_height, bar_idx = stack.pop()
            width = n - stack[-1][1] - 1
            rectangle = bar_height*width
            max_rectangle = max(max_rectangle, rectangle)
        
        return max_rectangle


        