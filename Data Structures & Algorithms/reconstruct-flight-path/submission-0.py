from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            flights[src].append(dst)
        
        stack = ['JFK']
        res = []
        
        while stack:
            curr = stack[-1]
            if not flights[curr]:
                res.append(stack.pop())
            else:
                stack.append(flights[curr].pop())
        
        return res[::-1]
        
