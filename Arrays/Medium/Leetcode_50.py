class Solution:
    def myPow(self, x: float, n: int) -> float:
        binform = n
        answer = 1
        if n < 0:
            x = 1/x
            binform = -binform
        while binform > 0:
            if binform % 2 == 1:
                answer *= x
            x *= x
            binform //= 2
        return answer