from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)

        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

    return result

def print_test_case(title, root):
    result = level_order_traversal(root)
    print(f"{title} : {result}")

# TEST CASES

# Case 1: Empty Tree
print_test_case("Test Case 1: Empty Tree", None)  # Expected: []

# Case 2: Single Node
single = TreeNode(10)
print_test_case("Test Case 2: Single Node Tree", single)  # Expected: [10]

# Case 3: Full Binary Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
print_test_case("Test Case 3: Full Binary Tree", root)  # Expected: [1, 2, 3, 4, 5, 6]