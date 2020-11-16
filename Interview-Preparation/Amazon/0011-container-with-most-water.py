class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i, j = 0, len(height)-1
        while i < j:
            curr_area = (j-i) * min(height[i], height[j])
            area = max(area, curr_area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return area
