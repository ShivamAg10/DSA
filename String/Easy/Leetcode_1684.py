class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        permutation = 0
        for i in s:
            permutation += abs(s.index(i) - t.index(i))
        return permutation