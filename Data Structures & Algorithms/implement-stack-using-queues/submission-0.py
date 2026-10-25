from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self._top_element = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self._top_element = x  

    def pop(self) -> int:
        
        while len(self.q1) > 1:
            self._top_element = self.q1.popleft()
            self.q2.append(self._top_element)
            
        
        popped = self.q1.popleft()
        
        
        self.q1, self.q2 = self.q2, self.q1
        return popped

    def top(self) -> int:
        return self._top_element

    def empty(self) -> bool:
        return not self.q1