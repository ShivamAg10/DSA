class Solution:
    def trap(self, height):
        leftWall = 0
        rightWall = 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        for i in range(len(height)):
            j = -i-1
            maxLeft[i] = leftWall
            maxRight[j] = rightWall
            leftWall = max(leftWall, height[i])
            rightWall = max(rightWall, height[j])
        
        summ = 0
        for i in range(len(height)):
            pot = min(maxLeft[i], maxRight[i])
            summ += max(0, pot - height[i])

        return summ

class Solution:
    def trap(self, height):
        Trapped_Water = 0
        for i in range(1, len(height)-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])
            minimum = min(left_max, right_max)
            area = minimum - height[i]
            if area > 0:
                Trapped_Water += area
        return Trapped_Water
# Time Limit Exceeded