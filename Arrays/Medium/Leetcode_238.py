class Solution:
    def productExceptSelf(self, nums):
        prod = 1
        for i in nums:
            if i != 0:
                prod *= i
        
        products = []
        count_zeros = nums.count(0)
        if count_zeros >= 2:
            products = [0] * len(nums)
        elif count_zeros == 1:
            for i in nums:
                if i != 0:
                    products.append(0)
                else:
                    products.append(prod)
        else:
            for i in nums:
                products.append(prod//i)
        return products
