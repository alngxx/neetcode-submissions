class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        # paths = ['', '...', 'a', '..', 'b', 'c', '..', 'd', '.', '']

        for cur in paths:
            # if encounter '..', pop current directory
            if cur == '..':
                if stack:
                    stack.pop()
            # don't push any '.' or '' to stack
            elif cur != '' and cur != '.':
                stack.append(cur)
        
        # stack = ['...', 'b', 'd']
        return "/" + "/".join(stack)