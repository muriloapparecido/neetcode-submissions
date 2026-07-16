class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+":
                stack.append(stack.pop() + stack.pop())
                continue
            if token in "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
                continue
            if token in "*":
                stack.append(stack.pop() * stack.pop())
                continue
            if token in "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
                continue
            stack.append(int(token))

        return stack[0]