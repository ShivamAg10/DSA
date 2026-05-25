class Solution:
    def findDuplicate(self, nums) -> int:
        stk = set()
        for i in nums:
            if i in stk:
                return i
            stk.add(i)