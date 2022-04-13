class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.is_last = False

class Trie():
    def __init__(self) -> None:
        self.root = TrieNode()


    def form(self, keys):
        for k in keys:
            self.insert(k)

    def insert(self, key):
        node = self.root

        for c in key:
            if not node.children.get(c):
                node.children[c] = TrieNode()

            node = node.children[c]
        node.last = True

    def suggestionRec(self, node, word):
        if node.is_last:
            print(word)
        
        for a, n in node.children.items():
            self.suggestionRec(n, word + a)
  
    def suggestions(self, key):
        node = self.root

        for c in key:
            if not node.children.get(c):
                return 0
            
            node = node.children[c]

        if not node.children:
            return -1
        
        self.suggestionRec(node, key)
        return 1