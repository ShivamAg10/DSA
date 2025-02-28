class Solution:
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals
        
        intervals.sort()
        
        start = intervals[0][0]
        end = intervals[0][1]
        output = []

        for s,e in intervals[1:]:
            if s <= end:
                end = max(e, end)
                if s < start:
                    start = s
            else:
                output.append([start, end])
                start = s
                end = e
        
        output.append([start, end])

        return output
