class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """ Stack: O(n), O(n)
        1. If it's a number: convert to int and push onto stack
        2. If it's an operator: push the result of (top 2 numbers and operator) onto stack
        3. After iterate all tokens, only final value left on stack
        """

        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                a, b = stack.pop(), stack.pop() 
                stack.append(b-a)      # a is pushed to stack after b
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) /a))
            else:
                stack.append(int(t))
        
        return stack[0]
        