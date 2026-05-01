class Solution:
    ops = '+-*/'

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(token, stack)
            if token not in Solution.ops:
                stack.append(int(token))
                continue
            
            arg2 = stack.pop()
            arg1 = stack.pop()
            if token == '+':
                result = arg1 + arg2
            elif token == '-':
                result = arg1 - arg2
            elif token == '*':
                result = arg1 * arg2
            else:
                result = int(arg1 / arg2)
            stack.append(result) 
        
        return stack[-1]