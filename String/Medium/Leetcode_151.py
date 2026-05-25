class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = words[::-1]
        rev = ""
        for word in words:
            rev += word + " "
        rev = rev[:-1]
        return rev