class trienode:
    def __init__(self):
        self.childrens = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = trienode()
    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.childrens:
                node.childrens[char] = trienode()
            node = node.childrens[char]
        node.is_end = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.childrens:
                return False
            node  = node.childrens[char]
        return node.is_end

    def search_using_prefix(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.childrens:
                return False
            node = node.childrens[char]
        return False
    def prefix_based_search(self,prefix):
        node = self.root

        for char in prefix:
            if char not in node.childrens:
                return []
            else:
                node = node.childrens[char]
        result = []
        self.dfs_for_words(node,prefix,result)
        return result
    def dfs_for_words(self,node,prefix,result):
        if node.is_end:
            result.append(prefix)
        for char,children  in node.childrens.items():
            self.dfs_for_words(children,prefix+char,result)


    def display(self):
        words = []
        self.dfs_for_words(self.root,"",words)
        return words

