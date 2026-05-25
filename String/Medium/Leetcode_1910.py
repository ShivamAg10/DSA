s = "aabababa"
part = "aba"
flag = True
while flag == True:
    if part in s:
        s = s.replace(part, "",1)
        print(s)
        continue
    flag = False