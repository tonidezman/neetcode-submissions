class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

    def lcp(self, word: str, prefixLen: int) -> int:
        node = self.root
        for i in range(min(len(word), prefixLen)):
            char = word[i]
            if char not in node.children:
                return i
            node = node.children[char]
        return min(len(word), prefixLen)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        # find the smallest word
        mini = 0
        for i in range(1, len(strs)):
            if mini > len(strs[i]):
                mini = i

        trie = Trie()
        trie.insert(strs[mini])
        prefixLen = len(strs[mini])
        for word in strs:
            prefixLen = trie.lcp(word, prefixLen)
        return strs[0][:prefixLen]
