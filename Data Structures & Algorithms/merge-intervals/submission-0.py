class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals:
            new_start = interval[0]
            new_end = interval[1]
            if new_start > end:
                res.append([start,end])
                start = new_start
                end = new_end
            else:
                end = max(end,new_end)
        res.append([start,end])
        return res

        