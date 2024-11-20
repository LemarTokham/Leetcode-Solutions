class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        # b - bracket
        for b in s:
            if b in brackets:
                # ensure stack is not empty before pop operation
                if stack and stack[-1] == brackets[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return (len(stack) == 0)