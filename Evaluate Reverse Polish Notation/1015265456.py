class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y - x)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(int(float(y) / x))
                case _:
                    stack.append(int(token))
 
        return stack.pop()
