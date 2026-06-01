class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:   
        # pop and add from stack 1 to stack 2 until only first element left
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        
        popleft = self.s1.pop()   # store res = queue.pop() before add all elements back to stack 1
        while self.s2:
            self.s1.append(self.s2.pop())
        return popleft

    def peek(self) -> int:
        # pop and add from stack 1 to stack 2 until only first element left
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        
        peek = self.s1[0]   # not remove, just return
        while self.s2:
            self.s1.append(self.s2.pop())
        return peek

    def empty(self) -> bool:
        return len(self.s1) == 0        


