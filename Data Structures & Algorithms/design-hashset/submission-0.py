class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyHashSet:

    def __init__(self):
        
        self.key_space = 2069
        self.buckets = [Node(0) for _ in range(self.key_space)]  

    def _hash(self, key: int) -> int:
        return key % self.key_space

    def add(self, key: int) -> None:
        hash_idx = self._hash(key)
        curr = self.buckets[hash_idx]
        while curr.next:
            if curr.next.val == key:
                return  
            curr = curr.next
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        hash_idx = self._hash(key)
        curr = self.buckets[hash_idx]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next  
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        hash_idx = self._hash(key)
        curr = self.buckets[hash_idx].next
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False