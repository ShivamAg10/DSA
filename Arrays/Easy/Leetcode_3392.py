class Solution:
    def countSubarrays(self, nums) -> int:
        if len(nums) < 3:
            return 0
        subarr = 0
        for i in range(len(nums)-2):
            curr = nums[i:i+3]
            if (curr[0]+curr[2]) == curr[1]/2:
                subarr += 1
        return subarr