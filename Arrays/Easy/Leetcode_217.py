class Solution:
    def containsDuplicate(self, nums):
        # count = {}
        # for i in nums:
        #     if i in count:
        #         count[i] += 1
        #     else:
        #         count[i] = 1
        # for i in count:
        #     if count[i] > 1:
        #         return True
        # return False

        notDuplicates = set()
        for i in nums:
            if i not in notDuplicates:
                notDuplicates.add(i)
            else:
                return True
        return False