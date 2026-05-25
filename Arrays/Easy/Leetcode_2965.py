class Solution:
    def findMissingAndRepeatedValues(self, grid):

        vis = [False] * len(grid) * len(grid)
        answer= [0,0]

        for r in range(0, len(grid)):
            for c in range(0, len(grid)):
                val = grid[r][c]
                if vis[val-1]==True:
                    answer[0] = val
                vis[val-1] = True
        
        for missingValue in range(0, len(vis)):
            if vis[missingValue]==False:
                answer[1] = missingValue+1
                break
        
        return answer
        