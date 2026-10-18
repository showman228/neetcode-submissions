class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dct = dict() # key: Node(key, val)

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        n_prev = self.tail.prev
        n_next = self.tail
        n_prev.next = n_next.prev = node
        node.next = n_next
        node.prev = n_prev


    def remove(self, node):
        n_prev, n_next = node.prev, node.next
        n_prev.next = n_next
        n_next.prev = n_prev

    def get(self, key: int) -> int:
        if key in self.dct:
            self.remove(self.dct[key])
            self.insert(self.dct[key])
            return self.dct[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self.remove(self.dct[key])
        self.dct[key] = Node(key, value)
        self.insert(self.dct[key])

        if len(self.dct) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.dct[lru.key]
