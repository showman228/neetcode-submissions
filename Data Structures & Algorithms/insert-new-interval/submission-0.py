class Solution:
    def insert_by_binary_search(self, intervals, newInterval) -> None:
        target = newInterval[0]
        left = 0
        right = len(intervals) - 1
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        intervals.insert(left, newInterval)        


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # вставить правильно newInterval не за nLogn
        # объединить интервалы которые пересекаются и вывести список intervals

        if not intervals:
            return [newInterval]

        self.insert_by_binary_search(intervals, newInterval)

        res = []
        for inter in intervals:
            if not res or res[-1][1] < inter[0]:
                res.append(inter)
            else:
                res[-1][1] = max(res[-1][1], inter[1])
        return res