class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        stack = []
        stack.append(-1)
        maxArea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i -stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
            
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        
        return maxArea
