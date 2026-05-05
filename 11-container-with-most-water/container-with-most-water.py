class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, (len(height) - 1)
        area = 0
        while i < j:
            area = max(min(height[i], height[j]) * (j - i), area)
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return area
