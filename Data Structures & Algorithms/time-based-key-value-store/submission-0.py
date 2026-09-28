class TimeMap:

    def __init__(self):
        self.timestamp_prev = 0
        self.dictionary = defaultdict(list) # имя: [значение, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timestamp_prev <= timestamp:
            self.timestamp_prev = timestamp
            self.dictionary[key] = [value, timestamp]

    def get(self, key: str, timestamp: int) -> str:
        sp = self.dictionary[key]
        return sp[0]
