class Solution:
    def calPoints(self, operations):
        lst = []
        count = -1
        # arr1 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
        for i in operations:
            if i == "C" and lst != []:
                lst.pop()
                count -= 1
            elif i == "D" and lst != []:
                lst.append(int(lst[count])*2)
                count += 1
            elif i == "+":
                lst.append(int(lst[count]) + int(lst[count-1]))
                count += 1
            else:
                lst.append(int(i))
                count += 1
        summ = 0
        for i in lst:
            summ += i
        return summ