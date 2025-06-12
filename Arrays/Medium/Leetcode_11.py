class Solution:
    def maxArea(self, height):
        maxArea = 0
        left = 0
        right = len(height)-1

        while left != right:
            maxArea = max((min(height[left], height[right]) * (right - left)), maxArea)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea