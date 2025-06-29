class Solution:
    def findMaxAverage(self, nums,k):
        maxAvg = currAvg = sum(nums[:k])
        pointer = 0

        for i in range(k, len(nums)):
            currAvg = currAvg - nums[pointer] + nums[i]
            maxAvg = max(maxAvg, currAvg)
            pointer += 1
        return maxAvg/k

nums = [1,2,3,4]
print(nums[1:2])