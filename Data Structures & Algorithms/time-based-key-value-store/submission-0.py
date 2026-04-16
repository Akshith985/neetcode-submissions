class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # Get the list of versions for this key
        values = self.store.get(key, [])
        
        # Binary Search for the largest timestamp <= given timestamp
        L, R = 0, len(values) - 1
        
        while L <= R:
            mid = (L + R) // 2
            # values[mid][0] is the timestamp
            if values[mid][0] <= timestamp:
                # This is a valid "past" or "present" value
                res = values[mid][1]
                # Try to see if there's a more recent one
                L = mid + 1
            else:
                # Too far in the future
                R = mid - 1
                
        return res
