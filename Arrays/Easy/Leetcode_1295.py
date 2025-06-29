class Solution:
    def findNumbers(self, nums):
        def calc_digi(number):
            digi = 0
            while number > 0:
                number = number // 10
                digi += 1
            return digi
        
        even_digi = 0

        for i in nums:
            digi = calc_digi(i)
            if digi % 2 == 0:
                even_digi += 1
        return even_digi

        # even_digi = 0
        # for i in nums:
        #     digi = len(str(i))
        #     if digi % 2 == 0:
        #         even_digi += 1
        # return even_digi