class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> str:
        res = []
        node = self.root
        for c in word:
            if c not in node.children:
                return "".join(res)
            res.append(c)
            node = node.children[c]
        return "".join(res)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        trie.insert(strs[0])
        res = strs[0]
        for word in strs:
            candidate = trie.search(word)
            if len(candidate) < len(res):
                res = candidate
        return "".join(res)
        