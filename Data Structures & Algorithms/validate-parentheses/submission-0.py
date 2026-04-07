class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        something = {"}": "{", ")": "(", "]":"["}
        for c in s:
            if c in something:
                if stack and stack[-1] == something[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False