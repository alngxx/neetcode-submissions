class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:   
        # pop and add from stack 1 to stack 2 until only front element left
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        # store pop value before add all elements back to stack 1
        popleft = self.s1.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        
        return popleft

    def peek(self) -> int:
        # pop and add from stack 1 to stack 2 until only front element left
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        
        # instead of pop, we only extract the front value
        peek = self.s1[0]
        while self.s2:
            self.s1.append(self.s2.pop())
        
        return peek


    def empty(self) -> bool:
        return len(self.s1) == 0 