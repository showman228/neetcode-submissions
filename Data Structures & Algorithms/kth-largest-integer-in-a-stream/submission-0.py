class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.q = deque()

        for elem in nums:
            self.q.append(elem)
        
        
    def add(self, val: int) -> int:
        res = self.q[self.k - 1]
        self.q.append(val)
        self.q.popleft()
        return res
        

