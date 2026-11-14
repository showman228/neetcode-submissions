"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            inter1 = intervals[i]
            for j in range(i + 1, len(intervals)):
                inter2 = intervals[j]
                if inter1.end > inter2.start:
                    return False
        return True