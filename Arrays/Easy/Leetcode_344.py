class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s)-1

        for i in range(0,len(s)//2):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        