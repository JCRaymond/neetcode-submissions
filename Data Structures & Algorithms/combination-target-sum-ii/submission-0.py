class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        def dfs(candidates_start, target):
            last_candidate = None
            for i in range(candidates_start, n):
                candidate = candidates[i]
                if candidate == last_candidate:
                    continue
                if candidate > target:
                    break
                if candidate == target:
                    yield [candidate]
                    break
                for combo in dfs(i+1, target-candidate):
                    yield [candidate, *combo]
                last_candidate = candidate
        
        return list(dfs(0, target))