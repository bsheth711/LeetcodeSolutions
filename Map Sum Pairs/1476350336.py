class MapSum:

    class Node:

        def __init__(self, letter = "", val = 0):
            self.letter = letter
            self.val = val
            self.children = {}
        
        def __repr__(self):
            return f"{{letter: {self.letter}, val: {self.val}, children: {self.children}}}"

    def __init__(self):
        self.root = self.Node()

    def insert(self, key: str, val: int) -> None:
        self.__builder(key, 0, self.root, val)

    def __builder(self, key, i, node, val): 
        if i >= len(key):
            node.val = val
            return
        if key[i] not in node.children:
            node.children[key[i]] = self.Node(key[i])
        
        self.__builder(key, i + 1, node.children[key[i]], val)

    def sum(self, prefix: str) -> int:
        curNode = self.root

        for c in prefix:
            if c not in curNode.children:
                return 0
            else:
                curNode = curNode.children[c]
        
        return self.__dfs(curNode)

    def __dfs(self, node):
        if not node.children:
            return node.val
        
        total = node.val
        
        for letter in node.children:
            total += self.__dfs(node.children[letter])
        
        return total
        
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)