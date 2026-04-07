class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                b = stack.pop()
                a = stack.pop()
                val = (eval(f"{a} {token} {b}"))
                if token == "/":
                    val = int(val)
                stack.append(val)
        return stack.pop()
