class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # count = {}
        # for i in magazine:
        #     if i in count:
        #         count[i] += 1
        #     else:
        #         count[i] = 1
        
        # for i in ransomNote:
        #     if i not in count or count[i] == 0:
        #         return False
        #     if i in count:
        #         count[i] -= 1
        # return True

        if len(ransomNote) > len(magazine):
            return False
        
        letters = set(ransomNote)

        for i in letters:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True