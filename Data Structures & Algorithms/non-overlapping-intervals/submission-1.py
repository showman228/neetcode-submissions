class Solution:
    def isMerge(self, inter1: List[int], inter2: List[int]) -> bool:
        return inter1[1] > inter2[0] or inter1 == inter2

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[0])
        sp = [intervals[0]]
        count = 0

        for inter in intervals:
            if sp[-1] == inter:
                continue
            
            if self.isMerge(sp[-1], inter):
                count += 1

        return count

