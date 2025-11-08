class Solution:
    def plusOne(self, digits):
        num = 0
        for i in digits:
            num = (num*10)+i
        num += 1
        arr = []
        while num > 0:
            arr.append(num%10)
            num = num // 10
        arr.reverse()
        return arr