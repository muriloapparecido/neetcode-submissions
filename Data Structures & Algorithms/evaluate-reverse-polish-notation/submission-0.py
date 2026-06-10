class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda a,b: a+b, 
            '-': lambda a,b: a-b, 
            '*': lambda a,b: a*b, 
            '/': lambda a,b: int(a/b)
            }
        stack = []
        for token in tokens:
            if token in operators:
                # pop two, apply, push result
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[token](a,b))

            else:
                stack.append(int(token))
        return stack[0]