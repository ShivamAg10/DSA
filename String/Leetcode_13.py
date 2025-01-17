class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        i = 0
        roman = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
        }
        while i<len(s)-1:
            if roman[s[i+1]] > roman[s[i]]:
                number += roman[s[i+1]] - roman[s[i]]
                i += 1
            else:
                number += roman[s[i]]
            i += 1
        if i < len(s):
            return number + roman[s[len(s) - 1]]
        return number