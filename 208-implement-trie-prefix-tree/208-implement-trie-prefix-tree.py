class TrieNode:
    def __init__(self, ch):
        self.ch = ""
        self.children = {} # maps ch -> TrieNode
        self.is_complete = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode("*") # init node
        

    def insert(self, word: str) -> None:
        root=self.root
        
        for ch in word:
            if ch in root.children:
                root=root.children[ch]
            else:
                root.children[ch]=TrieNode(ch)
                root=root.children[ch]
        root.is_complete=True
        

    def search(self, word: str) -> bool:
        root=self.root
        for ch in word:
            if ch in root.children:
                root=root.children[ch]
            else:
                return False
        return root.is_complete

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        
        for ch in prefix:
            if ch in root.children:
                root = root.children[ch]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)