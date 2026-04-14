class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            else:
                stack.append(eval(f"{stack.pop()} {token} {stack.pop()}"))
        return int(stack.pop())
