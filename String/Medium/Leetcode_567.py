class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        s2_freq = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1_freq[ord(s1[i])-97] += 1
            s2_freq[ord(s2[i])-97] += 1
        if s1_freq == s2_freq:
            return True
        
        j = len(s1)
        for i in range(len(s2)-len(s1)):
            s2_freq[ord(s2[i])-97] -= 1
            s2_freq[ord(s2[j])-97] += 1
            if s1_freq == s2_freq:
                return True
            j += 1
        return False