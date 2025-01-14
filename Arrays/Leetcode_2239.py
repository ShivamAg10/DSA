class Solution:
    def findClosestNumber(self, nums) -> int:
        closest = nums[0]
        for i in nums:
            if abs(i) < abs(closest):
                closest = i
        if closest<0 and abs(closest) in nums:
            return abs(closest)
        else: 
            return closest