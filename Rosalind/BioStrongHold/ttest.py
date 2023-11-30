class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.start = None
        self.end = None
        self.suffix_index = None

def print_tree(root, level=0):
    if root is None:
        return
    print('    ' * level + f'+-- {root[0]}')
    for child in root.children:
        print_tree(child, level+1)

def build_suffix_tree(word):
    root = SuffixTreeNode()
    n = len(word)
    for i in range(n):
        suffix = word[i:]
        current = root
        for j in range(len(suffix)):
            c = suffix[j]
            if c not in current.children:
                current.children[c] = SuffixTreeNode()
            current = current.children[c]
        current.suffix_index = i
    return root

# Example usage
word = "banana"
root = build_suffix_tree(word)
print(root.children)
print_tree(root)