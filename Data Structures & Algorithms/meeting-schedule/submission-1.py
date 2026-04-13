"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        events = []
        for obj in intervals:
            events.append((obj.start, obj.end))
        events.sort()
        i = 0
        for start, end in events[1:]:
            if start < events[i][1]:
                return False
            i+=1
        return True

            





        
