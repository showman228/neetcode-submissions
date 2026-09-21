class TimeMap:

    def __init__(self):
        self.dct = defaultdict(list) # timestamp: [имя, значение]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dct:
            self.dct[key] = []
        self.dct[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.dct.get(key, [])
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return res
