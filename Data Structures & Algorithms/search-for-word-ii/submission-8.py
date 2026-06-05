class PrefixTree:
    oa = ord('a')

    def __init__(self, prefix='', terminal=False):
        self.prefix = prefix
        self.letters = [None]*26
        self.terminal = terminal
        
    def insert(self, word: str) -> None:
        if word == '':
            self.terminal = True
            return
        c = word[0]
        idx = ord(c) - PrefixTree.oa

        if len(word) == 1 and self.letters[idx] is None:
            self.letters[idx] = True
            return
        if self.letters[idx] is None:
            self.letters[idx] = PrefixTree(prefix=self.prefix+c)
        elif self.letters[idx] is True:
            self.letters[idx] = PrefixTree(prefix=self.prefix+c)
            self.letters[idx].terminal = True
        self.letters[idx].insert(word[1:])

    def search_suffix(self, word: str) -> bool:
        if word == '':
            return self
        c = word[0]
        idx = ord(c) - PrefixTree.oa

        if self.letters[idx] is None:
            return PrefixTree.Null
        if self.letters[idx] is True:
            if len(word) == 1:
                return PrefixTree(prefix=self.prefix+c, terminal=True)
        return self.letters[idx].search_suffix(word[1:])

    @property
    def is_empty(self) -> bool:
        return self.terminal or any(self.letters)

PrefixTree.Null = PrefixTree()

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = PrefixTree()
        for word in words:
            root.insert(word)
        
        n = len(board)
        m = len(board[0])
        res = set()

        def dfs(r, c, prefix_tree):
            if r < 0 or r >= n or c < 0 or c >= m or board[r][c] == '*' or not prefix_tree.is_empty:
                return
            
            curr = board[r][c]
            board[r][c] = '*'
            prefix_tree = prefix_tree.search_suffix(curr)
            if prefix_tree.terminal:
                res.add(prefix_tree.prefix)
            
            dfs(r+1, c, prefix_tree)
            dfs(r-1, c, prefix_tree)
            dfs(r, c+1, prefix_tree)
            dfs(r, c-1, prefix_tree)

            board[r][c] = curr

        for r in range(n):
            for c in range(m):
                dfs(r, c, root)
        
        return list(res)



