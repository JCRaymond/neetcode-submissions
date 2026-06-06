from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        m =  len(beginWord)
        word_groups = defaultdict(list) 
        for word in wordList:
            for i in range(m):
                pattern = f'{word[:i]}*{word[i+1:]}'
                word_groups[pattern].append(word)
        
        stack = [(beginWord,1)]
        seen = set()
        seen.add(beginWord)
        while stack:
            curr, dist = stack.pop()

            for i in range(m):
                pattern = f'{curr[:i]}*{curr[i+1:]}'

                for similar in word_groups[pattern]:
                    if similar in seen:
                        continue
                    
                    if similar == endWord:
                        return dist + 1

                    seen.add(similar)
                    stack.append((similar, dist + 1))
        
        return 0