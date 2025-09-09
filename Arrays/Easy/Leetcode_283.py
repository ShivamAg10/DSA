class Solution:
    def moveZeroes(self, nums) -> None:
        answer = []
        for i in nums:
            if i!=0:
                answer.append(i)
        count_zeroes = nums.count(0)
        for i in range(0, len(answer)):
            nums[i] = answer[i]
        for i in range(len(answer), len(nums)):
            nums[i] = 0