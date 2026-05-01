class MinStack:

    def __init__(self):
        self.vals = []
        

    def push(self, val: int) -> None:
        new_min = val
        if len(self.vals) > 0:
            old_min = self.vals[-1][1]
            new_min = min(val, old_min)

        self.vals.append((val, new_min))
        

    def pop(self) -> None:
        self.vals.pop()
        

    def top(self) -> int:
        return self.vals[-1][0]
        

    def getMin(self) -> int:
        return self.vals[-1][1]
        
