class ListNode:
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.buckets = [ListNode() for _ in range(self.key_space)]  

    def _hash(self, key: int) -> int:
        return key % self.key_space

    def put(self, key: int, value: int) -> None:
        hash_idx = self._hash(key)
        curr = self.buckets[hash_idx]
        
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value  
                return
            curr = curr.next
            
        curr.next = ListNode(key, value)  

    def get(self, key: int) -> int:
        hash_idx = self._hash(key)
        curr = self.buckets[hash_idx].next
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
            
        return -1

    def remove(self, key: int) -> None:
        hash_idx = self._hash(key)
        curr = self.buckets[hash_idx]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next  
                return
            curr = curr.next