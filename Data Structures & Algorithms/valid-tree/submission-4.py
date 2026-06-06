class UnionNode:

    def __init__(self, val, is_root=False):
        self.val = val
        self.children = []


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [list() for _ in range(n)]
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        stack = [(0,-1)]
        seen = [False]*n
        seen[0] = True
        while stack:
            curr, parent = stack.pop()

            for neighbor in graph[curr]:
                if neighbor == parent:
                    continue
                
                if seen[neighbor]:
                    return False
                
                seen[neighbor] = True
                stack.append((neighbor, curr))
            
        return all(seen)

        