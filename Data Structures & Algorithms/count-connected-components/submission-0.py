class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        components = 0
        seen = [False]*n
        i = 0
        while i < n:
            while i < n and seen[i]:
                i += 1
            if i == n:
                break
            components += 1
            
            seen[i] = True
            stack = [i]
            while stack:
                curr = stack.pop()

                for neighbor in graph[curr]:
                    if seen[neighbor]:
                        continue
                    seen[neighbor] = True
                    stack.append(neighbor)
        
        return components