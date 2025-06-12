class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
# Time Complexity: 81.39%
# Space Complexity: 95.24%

s = "A man, a plan, a canal: Panama"
s = s.lower()
new_s = ""
for i in s:
    if i.isalnum():
        new_s += i
print(s)
print(new_s)
print(new_s == new_s[::-1])
# Time Complexity: 81.39%
# Space Complexity: 56.93%