class Solution:
    def maxScore(self, s: str) -> int:
        maximum = 0
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]
            if (left.count("0")) + (right.count("1")) > maximum:
                maximum = (left.count("0")) + (right.count("1"))
        return maximum