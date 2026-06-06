from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        edge_map = dict(map(reversed, enumerate(map(tuple, edges))))
        
        start = next(iter(graph))
        parent = {}
        parent[start] = start
        stack = [start]
        while stack:
            curr = stack.pop()

            for neighbor in graph[curr]:
                if neighbor == parent[curr]:
                    continue
                
                if neighbor not in parent:
                    parent[neighbor] = curr
                    stack.append(neighbor)
                    continue

                edge = tuple(sorted([curr, neighbor]))
                edge_idx = edge_map[edge]
                
                temp = curr
                while parent[temp] != temp:
                    temp_edge = tuple(sorted([temp, parent[temp]]))
                    temp_edge_idx = edge_map[temp_edge]

                    if temp_edge_idx > edge_idx:
                        edge = temp_edge
                        edge_idx = temp_edge_idx
                    
                    temp = parent[temp]

                temp = neighbor
                while parent[temp] != temp:
                    temp_edge = tuple(sorted([temp, parent[temp]]))
                    temp_edge_idx = edge_map[temp_edge]

                    if temp_edge_idx > edge_idx:
                        edge = temp_edge
                        edge_idx = temp_edge_idx
                    
                    temp = parent[temp]

                return list(edge)
