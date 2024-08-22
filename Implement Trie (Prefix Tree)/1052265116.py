class Trie:

    class Node:

        def __init__(self, val = None):
            # char: Node
            self.children = {}
            self.val = val
            self.terminal = False

    def __init__(self):
        self.root = self.Node() 

    def insert(self, word: str) -> None:
        cur = self.root
        s = ''

        for c in word:
            s += c

            if s in cur.children:
                cur = cur.children[s]
            else:
                cur.children[s] = self.Node(s)
                cur = cur.children[s]

            if cur.val == word:
                cur.terminal = True

    def search(self, word: str) -> bool:
        cur = self.root
        s = ''

        for c in word:
            s += c

            if s in cur.children:
                cur = cur.children[s]
                if cur.val == word and cur.terminal:
                    return True
            else:
                return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        s = ''

        for c in prefix:
            s += c

            if s in cur.children:
                cur = cur.children[s]
                if cur.val == prefix:
                    return True
            else:
                return False
       


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)