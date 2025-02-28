class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return nums
        finalAnswer = []
        start = nums[0]
        i = 0
        while i < len(nums)-1:
            if nums[i+1] - nums[i] != 1:
                if i == nums.index(start):
                    finalAnswer.append(str(start))
                else:
                    finalAnswer.append(str(start) + "->" + str(nums[i]))
                start = nums[i+1]
            i += 1
        if start == nums[len(nums)-1]:
            finalAnswer.append(str(start))
        else:
            finalAnswer.append(str(start) + "->" + str(nums[i]))
        return finalAnswer
        