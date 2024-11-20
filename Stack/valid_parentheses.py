class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            # pushing open brackets to stack
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                # ensuring stack is not empty to avoid stack underflow error
                if len(stack) == 0:
                    return False
                # compare closed bracket with top of stack, if they are same type, then valid bracket, if not, we return false
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop() 
                    else:
                        return False
                elif s[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif s[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        # if the stack is empty we have removed every bracket, which is only the case when valid pairs are found, so if it is empty, every bracket was valid
        return (len(stack) == 0)


