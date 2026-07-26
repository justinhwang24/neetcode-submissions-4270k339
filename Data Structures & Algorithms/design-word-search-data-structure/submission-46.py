class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, cur):
            if j == len(word):
                return cur.word
            if word[j] == '.':
                for c in cur.children.values():
                    if dfs(j + 1, c):
                        return True
                return False
            else:
                if word[j] not in cur.children:
                    return False
            return dfs(j + 1, cur.children[word[j]])

        return dfs(0, self.root)