class PrefixTree:
    oa = ord('a')

    def __init__(self):
        self.letters = [None]*26
        self.terminal = False
        
    def insert(self, word: str) -> None:
        if word == '':
            self.terminal = True
            return
        idx = ord(word[0]) - PrefixTree.oa
        if len(word) == 1 and self.letters[idx] is None:
            self.letters[idx] = True
            return
        if self.letters[idx] is None:
            self.letters[idx] = PrefixTree()
        elif self.letters[idx] is True:
            self.letters[idx] = PrefixTree()
            self.letters[idx].terminal = True
        self.letters[idx].insert(word[1:])

    def search(self, word: str) -> bool:
        if word == '':
            return self.terminal
        idx = ord(word[0]) - PrefixTree.oa

        if self.letters[idx] is None:
            return False
        if self.letters[idx] is True:
            return len(word) == 1
        return self.letters[idx].search(word[1:])
        

    def startsWith(self, prefix: str) -> bool:
        if prefix == '':
            return any(letter is not None for letter in self.letters) or self.terminal
        idx = ord(prefix[0]) - PrefixTree.oa

        if self.letters[idx] is None:
            return False
        if self.letters[idx] is True:
            return len(prefix) == 1
        return self.letters[idx].startsWith(prefix[1:])
        