class Solution:
    def interchangeableRectangles(self, rectangles):
        count = 0

        # for i in range(len(rectangles)-1):
        #     for j in range(i+1, len(rectangles)):
        #         if (rectangles[i][0]/rectangles[i][1])==(rectangles[j][0]/rectangles[j][1]):
        #             count += 1
        # return count

        # arr = []
        # for i in rectangles:
        #     arr.append(i[0]/i[1])
        # similarities_mapping = {}
        # for i in arr:
        #     if i in similarities_mapping:
        #         similarities_mapping[i] += 1
        #     else:
        #         similarities_mapping[i] = 1
        # for i in similarities_mapping:
        #     for j in range(similarities_mapping[i]-1, 0, -1):
        #         count += j
        # return count

        mapping = {}
        for i, j in rectangles:
            k = i / j
            if k in mapping:
                count += mapping[k]
                mapping[k] += 1
            else:
                mapping[k] = 1
        return count