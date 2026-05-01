class Solution:
    open_brackets = set('({[')
    corres_open = {
        '}':'{',
        ']':'[',
        ')':'('

    }

    def isValid(self, s: str) -> bool:
        stack = []
        for car in s:
            if car in Solution.open_brackets:
                stack.append(car)
                continue
            
            if len(stack) == 0 or stack[-1] != Solution.corres_open[car]:
                return False
            
            stack.pop()
        
        return len(stack) == 0