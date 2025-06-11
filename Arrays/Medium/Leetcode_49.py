from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        answer = []
        anagram_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagram_dict[key].append(s)
        for i in anagram_dict:
            answer.append(anagram_dict[i])
        return answer