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