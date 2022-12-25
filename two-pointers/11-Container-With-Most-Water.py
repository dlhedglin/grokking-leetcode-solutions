class Solution:
    def maxArea(self, height: List[int]) -> int:
        start,end = 0, len(height) - 1
        maxArea = float('-inf')

        while (start < end):
            dist = end-start
            minHeight = min(height[start], height[end])
            maxArea = max(maxArea, minHeight * dist)

            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                start +=1
                end -= 1
        return maxArea