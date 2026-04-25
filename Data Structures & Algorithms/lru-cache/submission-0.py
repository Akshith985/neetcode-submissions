class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map keys to Nodes
        
        # Dummy nodes to avoid null checks
        # left.next will be LRU | right.prev will be MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Helper: Remove a node from the middle of the chain
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Helper: Insert a node at the right (Most Recently Used)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # 1. It's used, so move it to the front (MRU)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # 1. If key exists, we are updating, so remove the old node version
        if key in self.cache:
            self.remove(self.cache[key])
        
        # 2. Create new node and move to front (MRU)
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # 3. If we exceeded capacity, evict the LRU (the one at left.next)
        if len(self.cache) > self.cap:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key] # Delete from map using the node's key
        
