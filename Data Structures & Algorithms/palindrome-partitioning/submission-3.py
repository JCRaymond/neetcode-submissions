from functools import lru_cache

class Solution:
    def is_palindrome(self, s: str, start=0, end=None):
        end = (end or len(s))-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
            

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        @lru_cache
        def dfs(start):
            return list(dfs_gen(start))

        def dfs_gen(start):
            if start >= n:
                yield ''
                return
            if start == n-1:
                yield [s[start]]
                return
            
            for new_start in range(start+1, n+1):
                if self.is_palindrome(s, start, new_start):
                    pali_prefix = s[start: new_start]
                    for pali_part in dfs(new_start):
                        yield [pali_prefix, *pali_part]
        
        return dfs(0)
