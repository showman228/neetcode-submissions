class TimeMap:

    def __init__(self):
        self.timestamp_prev = 0
        self.dct = defaultdict(list) # имя: [значение, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timestamp_prev <= timestamp:
            self.timestamp_prev = timestamp
            self.dct[key] = [value, timestamp]

    def get(self, key: str, timestamp: int) -> str:
        sp = self.dct[key]
        if sp and self.timestamp_prev <= timestamp:
            return sp[0]
        return ""
