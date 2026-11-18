"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        res = 0
        lst_start = sorted([inter.start for inter in intervals])   
        lst_end = sorted([inter.end for inter in intervals])
        p_s = 0
        p_e = 0
        while p_s < len(intervals):
            if lst_start[p_s] < lst_end[p_e]:
                p_s += 1
                count += 1
            else:
                p_e += 1 
                count -= 1     

            res = max(res, count)
        return res
