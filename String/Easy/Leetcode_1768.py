class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstr = ""
        for i in range(0, min(len(word1), len(word2))):
            newstr += (word1[i]+word2[i])
        if len(word1) == len(word2):
            return newstr
        if len(word1) > len(word2):
            for i in range(len(word2), len(word1)):
                newstr += word1[i]
            return newstr
        if len(word1) < len(word2):
            for i in range(len(word1), len(word2)):
                newstr += word2[i]
            return newstr