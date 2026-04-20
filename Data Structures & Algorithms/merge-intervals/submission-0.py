class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        temp = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            prev_start = temp[0]
            prev_end = temp[1]
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            if curr_start <= prev_end:
                temp = [prev_start, max(prev_end, curr_end)]
            else:
                res.append([prev_start, prev_end])
                temp = [curr_start, curr_end]
        res.append(temp)
        return res





        