class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        while stack:
            curr, start = stack.pop()
            for i in range(start, len(word)):
                c = word[i]
                if c != '.':
                    if c not in curr.children:
                        break
                    curr = curr.children[c]
                else:
                    for sub_trie in curr.children.values():
                        stack.append((sub_trie, i+1))
                    break
            else:
                if curr.word:
                    return True
        return False
