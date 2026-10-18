class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.sp = []

    def get(self, key: int) -> int:
        for i in range(len(self.sp)):
            if self.sp[i][0] == key:
                tmp = self.sp.pop(i)
                self.sp.append(tmp)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.sp)):
            if self.sp[i][0] == key:
                tmp = self.sp.pop(i)
                tmp[1] = value
                self.sp.append(tmp)

        if len(self.sp) == self.capacity:
            self.sp.pop(0)
            
        self.sp.append([key, value])


