from functools import lru_cache

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        @lru_cache
        def dfs(size):
            return list(dfs_gen(size))

        def dfs_gen(size):
            if size == 0:
                yield ''
                return
            if size == 2:
                yield '()'
                return
            
            for close in range(1, size, 2):
                for parens1 in dfs(close - 1):
                    for parens2 in dfs(size - close - 1):
                        yield '(' + parens1 + ')' + parens2
        
        return list(dfs(n * 2))