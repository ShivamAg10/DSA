class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # return s == s[::-1]
        # Time Complexity : 80.04% : 4ms
        # Space Complexity: 19.54% : 17.91MB

        original_x = x

        if x<0 or (x%10==0 and x!=0):
            return False
        
        rev_num = 0
        while x > 0:
            rem = x % 10
            rev_num = (rev_num * 10) + rem
            x //= 10
        
        return original_x == rev_num

        # Time Complexity : 43.75% : 9ms
        # Space Complexity: 63.93% : 17.78MB