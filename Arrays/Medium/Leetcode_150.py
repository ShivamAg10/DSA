class Solution:
    def evalRPN(self, tokens):
        num = []
        for i in range(0,len(tokens)):
            if tokens[i] == '+':
                answer = num[len(num)-1] + num[len(num)-2]
                num.pop()
                num.pop()
                num.append(answer)
            elif tokens[i] == '-':
                answer = num[len(num)-2] - num[len(num)-1]
                num.pop()
                num.pop()
                num.append(answer)
            elif tokens[i] == '*':
                answer = num[len(num)-1] * num[len(num)-2]
                num.pop()
                num.pop()
                num.append(answer)
            elif tokens[i] == '/':
                answer = int(num[len(num)-2] / num[len(num)-1])
                num.pop()
                num.pop()
                num.append(answer)
            else:
                num.append(int(tokens[i]))
        return num[0]