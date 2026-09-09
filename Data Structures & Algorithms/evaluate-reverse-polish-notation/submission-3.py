class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == '+':
                stack.append(stack.pop()+stack.pop())
            elif ch == '-':
                second, first = stack.pop(), stack.pop()
                stack.append(first-second)
            elif ch == '*':
                stack.append(stack.pop()*stack.pop())
            elif ch == '/':
                second, first = stack.pop(), stack.pop()
                stack.append(int(first/second))
            else:
                stack.append(int(ch))

        return stack.pop()
        