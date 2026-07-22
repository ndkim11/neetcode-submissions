class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp_min = self.stack[0]
        for i in range(1, len(self.stack)):
            if self.stack[i] < temp_min:
                temp_min = self.stack[i]

        return temp_min
