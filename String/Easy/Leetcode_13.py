class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        numeral = 0
        i = 0
        while i<len(s)-1:
            if roman[s[i+1]] > roman[s[i]]:
                numeral += (roman[s[i+1]] - roman[s[i]])
                i += 2
            else:
                numeral += roman[s[i]]
                i += 1
        if i == len(s):
            return numeral
        else:
            numeral += roman[s[-1]]
            return numeral