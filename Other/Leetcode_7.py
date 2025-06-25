class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        revNum = 0
        while num > 0:
            rem = num % 10  
            revNum = (revNum * 10) + rem
            num //= 10
        if revNum >= 2**31:
            return 0
        return revNum if x > 0 else (0-revNum)