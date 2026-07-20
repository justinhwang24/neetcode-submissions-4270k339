class TrieNode:
    def __init__(self):
        self.chars = [None] * 26
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.chars[i]:
                cur.chars[i] = TrieNode()
            cur = cur.chars[i]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.chars[i]:
                return False
            cur = cur.chars[i]
        return cur.word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not cur.chars[i]:
                return False
            cur = cur.chars[i]
        return True
        