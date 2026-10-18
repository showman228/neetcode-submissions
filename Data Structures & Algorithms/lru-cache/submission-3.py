class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.sp = [] # [key, value]

    def get(self, key: int) -> int:
        for i in range(len(self.sp)):
            if self.sp[i][0] == key:
                temp = self.sp.pop(i)
                self.sp.append(temp)
                return temp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.sp)):
            if self.sp[i][0] == key:
                temp = self.sp.pop(i)
                temp[1] = value
                self.sp.append(temp)
        
        if len(self.sp) == self.capacity:
            self.sp.pop(0)
        
        self.sp.append([key, value])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)