class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)<=1:
            return 0
        intervals.sort(key = lambda x :x[0] )
        result=[intervals[0]]
        for i in range (1,len(intervals)):
            current,last = intervals[i][0] , intervals[i][1]
            prev_current , prev_last = result[-1][0] , result[-1][1]
            if current<prev_last:
                result[-1][1] = min(last,prev_last)
            else :
                result.append(intervals[i])
        return len(intervals) - len(result)