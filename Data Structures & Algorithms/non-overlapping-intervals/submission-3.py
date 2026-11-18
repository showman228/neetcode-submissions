class Solution:
    def isMerge(self, inter1: List[int], inter2: List[int]) -> bool:
        return inter1[1] > inter2[0] 

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x[1])
        sp = [intervals[0]]
        count = 0

        for inter in intervals[1:]:
            
            if self.isMerge(sp[-1], inter):
                count += 1
            else:
                sp.pop()
                sp.append(inter)

        return count

