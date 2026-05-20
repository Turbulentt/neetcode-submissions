"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        currVal = 0
        for x in intervals:
            if x.start < currVal:
                return False
            currVal = x.start
            if x.end < currVal:
                return False
            currVal = x.end

        return True