class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        mergedArr = nums1 + nums2
        mergedArr.sort()

        if len(mergedArr) % 2 != 0:
            median_idx = (len(mergedArr)//2)
            return mergedArr[median_idx]
        else:
            return (mergedArr[len(mergedArr)//2] + mergedArr[(len(mergedArr)//2) -1]) / 2