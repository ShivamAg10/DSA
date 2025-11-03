class Solution:
    def searchMatrix(self, matrix,target: int) -> bool:
        # for i in matrix:
        #     for j in i:
        #         if j == target:
        #             return True
        # return False

        for i in matrix:
            if target in i:
                return True
        return False