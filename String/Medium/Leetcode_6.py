class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            return s[::2] + s[1::2]
        lst = [""]*numRows
        rev = False
        count = 0
        for i in s:
            if rev == False:
                lst[count] += i
                count += 1
                if count == numRows:
                    rev = True
                    count -= 2
            else:
                lst[count] += i
                count -= 1
                if count == 0:
                    rev = False
        outputStr = ""
        return "".join(lst)