class Solution:
    def constructTransformedArray(self, nums):
        result = [0] * len(nums)
        for i in range(0, len(nums)):
            idx = (i + nums[i]) % len(nums)
            result[i] = nums[idx]
        return result