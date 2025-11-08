class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        # odd - True
        isodd = []
        for i in arr:
            if i%2 != 0:
                isodd.append(i)
                if len(isodd) == 3:
                    return True
            else:
                isodd.clear()
        return False