class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i, interval in enumerate(intervals):
            if len(res) == 0:
                res.append(interval)
            else:
                curInterval = res[-1]
                if curInterval[1] >= interval[0]:
                    ## if cur interval fits in last interval in res
                    res[-1][1] = max(interval[1], res[-1][1])
                else:
                    res.append(interval)
        return res