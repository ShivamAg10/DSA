class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer = m
        for i in range(0,n):
            nums1[pointer] = nums2[i]
            pointer += 1

        nums1.sort()
        