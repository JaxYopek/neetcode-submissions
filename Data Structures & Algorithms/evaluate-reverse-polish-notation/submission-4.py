class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                val = (f"{a} {token} {b}")
                if token == "/":
                    val = int(val)
                stack.append(val)
        return stack.pop()
