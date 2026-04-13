"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for obj in intervals:
            events.append((obj.start, 1))
            events.append((obj.end, -1))
        events.sort(key = lambda x: (x[0], x[1]))
        meeting_room = 0
        res = 0

        for _ , val in events:
            meeting_room += val
            res = max(res, meeting_room)
        return res



        