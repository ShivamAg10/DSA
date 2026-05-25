class Solution:
    def singleNumber(self, nums) -> int:
        temp = 0
        for i in nums:
            temp = temp^i
        return temp