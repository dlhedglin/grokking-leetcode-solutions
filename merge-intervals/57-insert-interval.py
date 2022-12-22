class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res = []
        for i, interval in enumerate(intervals):
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            print(interval)
            if newInterval[1] < interval[0]:
                #new interval comes before current interval
                res.append(newInterval)
                newInterval = interval
            elif newInterval[0] > interval[1]:
                # new interval comes after current interval
                res.append(interval)
            else:
                # new interval overlaps current interval
                newInterval[1] = max(interval[1], newInterval[1])
                newInterval[0] = min(interval[0], newInterval[0])
        res.append(newInterval)
        return res
