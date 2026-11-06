class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.maxHeap, num)

        while len(self.maxHeap) > k:
            heapq.heappop(self.maxHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > self.k:
            heapq.heappop(self.maxHeap)
        return self.maxHeap[0]

