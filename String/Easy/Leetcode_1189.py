import collections 

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_text_chars = collections.Counter(text)
        balloon = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0
        }
        for i in count_text_chars:
            if i in balloon:
                balloon[i] = count_text_chars[i]
        b = balloon['b']
        a = balloon['a']
        l = balloon['l'] // 2
        o = balloon['o'] // 2
        n = balloon['n']

        return min(b,a,l,o,n)