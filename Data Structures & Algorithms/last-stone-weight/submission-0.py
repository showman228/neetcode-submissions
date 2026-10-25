import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            if a < b:
                heapq.heappush(heap, -(b - a))
            else:
                heapq.heappush(heap, -(a - b))

        return -heap[0] if heap else 0