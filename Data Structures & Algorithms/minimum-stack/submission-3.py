class MinStack:
    """ Two Stacks: O(1), O(n)
    - Instead of search the whole stack to find min, we can keep a second stack
    that always store min value up to that level
    - So whenever push a new value, compare it with current min and push smaller one onto min_stack
    - Thus, top of min_stack is always min of entire stack
    E.g. push(1), push(2), push(0):
    stack = [1, 2, 0]
    min_stack = [1, 1, 0]
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)                    # push new value to stack

        if self.min_stack:
            val = min(val, self.min_stack[-1])    # update new minimum
        self.min_stack.append(val)                # push new minimum to min_stack

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]            # return current minimum, which is on min_stack