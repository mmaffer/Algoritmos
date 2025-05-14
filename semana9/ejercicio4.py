# -------------------------
# Node class for the generic tree
# -------------------------
class GenericTreeNode:
    def __init__(self, value):
        self.value = value        # Value of the node
        self.children = []        # List of child nodes

# -------------------------
# Generic tree class
# -------------------------
class GenericTree:
    """Generic tree implementation"""

    def __init__(self, root=None):
        self.root = root  # Root node of the tree

    def find_leaves(self):
        """Find all leaf nodes in the tree"""
        leaves = []

        def dfs(node):
            if node is None:
                return
            if not node.children:          # If the node has no children, it's a leaf
                leaves.append(node.value)
            for child in node.children:    # Recursively visit each child
                dfs(child)

        dfs(self.root)  # Start traversal from the root
        return leaves

# -------------------------
# Test 1: Empty tree
# Tree: None
empty_tree = GenericTree(None)
print(empty_tree.find_leaves() == [])  # 📭 No leaves expected

# -------------------------
# Test 2: Single node (root is a leaf)
# Tree: X
single = GenericTree(GenericTreeNode('X'))
print(single.find_leaves() == ['X'])  # 🌱 Root is the only leaf

# -------------------------
# Test 3: Linear tree
# Tree: A → B → C
linear_root = GenericTreeNode('A')
linear_b = GenericTreeNode('B')
linear_c = GenericTreeNode('C')
linear_root.children = [linear_b]
linear_b.children = [linear_c]
linear_tree = GenericTree(linear_root)
print(linear_tree.find_leaves() == ['C'])  # 🍃 Only C is a leaf

# -------------------------
# Test 4: Multiple leaves
# Tree:
#        A
#      / | \
#     B  C  D
#    /|\     \
#   E F G     H
tree_root = GenericTreeNode('A')
b, c, d = GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D')
e, f, g, h = GenericTreeNode('E'), GenericTreeNode('F'), GenericTreeNode('G'), GenericTreeNode('H')
tree_root.children = [b, c, d]
b.children = [e, f, g]
d.children = [h]
tree = GenericTree(tree_root)
print(sorted(tree.find_leaves()) == ['C', 'E', 'F', 'G', 'H'])  # 🍂 Expected leaves

# -------------------------
# Test 5: Wide tree (all children are leaves)
# Tree:
#        A
#   / / / | \ \
#  B  C  D  E  F
wide_root = GenericTreeNode('A')
wide_root.children = [
    GenericTreeNode('B'),
    GenericTreeNode('C'),
    GenericTreeNode('D'),
    GenericTreeNode('E'),
    GenericTreeNode('F')
]
wide_tree = GenericTree(wide_root)
print(sorted(wide_tree.find_leaves()) == ['B', 'C', 'D', 'E', 'F'])  # 🌿 All children are leaves