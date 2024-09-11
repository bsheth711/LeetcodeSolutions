class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort()
        curEnd = intervals[0][1]
        numToRemove = 0

        for start, end in intervals[1:]:
            if start < curEnd:
                numToRemove += 1
                curEnd = min(curEnd, end)
            else:
                curEnd = end
 
        return numToRemove