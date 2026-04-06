class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        cmds=["MinStack","push","getMin",]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if val<self.min_stack[-1]:
                minimum=val
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
