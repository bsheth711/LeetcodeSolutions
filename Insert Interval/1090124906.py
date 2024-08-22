class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        overlapping = []
        res = []

        for interval in intervals:
            if newInterval[0] >= interval[0] and newInterval[1] <= interval[1]:
                return intervals
            elif newInterval[0] >= interval[0] and newInterval[0] <= interval[1]:
                overlapping.append(interval)
            elif newInterval[0] <= interval[0] and newInterval[1] >= interval[1]:
                overlapping.append(interval)
            elif newInterval[1] >= interval[0] and newInterval[1] <= interval[1]:
                overlapping.append(interval)
            else:
                res.append(interval)
        
        start = newInterval[0]
        end = newInterval[1]
        
        if overlapping:
            start = min(start, overlapping[0][0])
            end = max(end, overlapping[-1][1])
        
        if not res:
            return [[start, end]]

        for i in range(len(res)):
            cur = res[i]

            if cur[0] > start:
                res.insert(i, [start, end])
                break
            
            if i == len(res) - 1:
                res.append([start, end])
        
        return res
    




