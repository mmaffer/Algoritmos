class Node:
    def __init__(self, value):
        self.value = value          # Store the value of the node (operand or operator)
        self.left = None            # Left child (for operators, left operand)
        self.right = None           # Right child (for operators, right operand)

def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""

    # Define operator precedence: * and / have higher precedence than + and -
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    output = []     # List to store the postfix expression result
    stack = []      # Stack to temporarily hold operators and parentheses

    # Iterate through each token in the infix list
    for token in tokens:
        if token.isalnum():          # If token is an operand (number or letter)
            output.append(token)     # Add operand directly to output list

        elif token == '(':           # If token is a left parenthesis
            stack.append(token)      # Push it onto the stack

        elif token == ')':           # If token is a right parenthesis
            # Pop operators from stack to output until left parenthesis is found
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()              # Remove the '(' from the stack (discard it)

        else:
            # Token is an operator (+, -, *, /)
            # Pop from stack to output while top of stack has operator of higher or equal precedence
            while stack and stack[-1] != '(' and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)      # Push current operator onto the stack

    # After all tokens processed, pop any remaining operators to output
    while stack:
        output.append(stack.pop())

    return output   # Return the postfix expression list

def build_expression_tree(postfix_tokens):
    stack = []      # Stack to hold nodes while building the tree

    # Iterate through each token in postfix expression
    for token in postfix_tokens:
        if token.isalnum():           # If operand, create a node and push to stack
            stack.append(Node(token))
        else:
            # Token is an operator: pop two nodes for operands
            right = stack.pop()       # Right operand node
            left = stack.pop()        # Left operand node
            new_node = Node(token)    # Create new operator node
            new_node.left = left      # Assign left child
            new_node.right = right    # Assign right child
            stack.append(new_node)    # Push this subtree root back to stack

    return stack[0]  # The last node in stack is root of the expression tree

def inorder_traversal(node):
    if node is None:
        return ''                   # Base case: empty node returns empty string

    # If node has children, it's an operator — add parentheses to clarify order
    if node.left and node.right:
        # Recursively get string of left subtree + operator + right subtree
        return f'({inorder_traversal(node.left)} {node.value} {inorder_traversal(node.right)})'

    return node.value              # Leaf node (operand), return its value directly

# --- Test cases ---

# ➕ Simple addition
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])

# 📊 Operator precedence: multiplication before addition
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])

# 🔗 Parentheses change precedence
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])

# 🧮 More complex expression with two grouped subexpressions
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])

# 🔤 Multiple operators and variables
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])
