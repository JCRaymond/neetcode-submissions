from functools import lru_cache

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [list(nums)]
        n = len(nums)
        permutations = []
        curr = list(nums)

        def dfs(prefix_len):
            if prefix_len == n-2:
                permutations.append(list(curr))
                curr[prefix_len], curr[prefix_len+1] = curr[prefix_len+1], curr[prefix_len]
                permutations.append(list(curr))
                curr[prefix_len], curr[prefix_len+1] = curr[prefix_len+1], curr[prefix_len]
                return
            
            dfs(prefix_len+1)
            for i in range(prefix_len+1, n):
                curr[prefix_len], curr[i] = curr[i], curr[prefix_len]
                dfs(prefix_len+1)
                curr[prefix_len], curr[i] = curr[i], curr[prefix_len]
        
        dfs(0)
        return permutations
            
            
