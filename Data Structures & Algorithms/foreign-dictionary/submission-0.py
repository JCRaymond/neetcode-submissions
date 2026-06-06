from collections import deque
from itertools import zip_longest

class Solution:
    oa = ord('a')

    def foreignDictionary(self, words: List[str]) -> str:
        letters = set(c for word in words for c in word)
        followers = {c: set() for c in letters}
        indegree = {c: 0 for c in letters}

        next_word_it = iter(words)
        next(next_word_it)
        for before, after in zip(words, next_word_it):
            for bc, ac in zip_longest(before, after, fillvalue=None):
                if ac is None:
                    return ''
                if bc is None:
                    break
                if bc != ac:
                    if ac not in followers[bc]:
                        followers[bc].add(ac)
                        indegree[ac] += 1
                    break

        q = deque([c for c, deg in indegree.items() if deg == 0])
        res = []

        while q:
            curr = q.popleft()
            res.append(curr)
            for neighbor in followers[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(res) != len(letters):
            return ''
        
        return ''.join(res)
