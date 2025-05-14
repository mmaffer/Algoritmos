def infix_to_postfix(tokens):
    """Convert infix expression to postfix notation"""
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Stack to hold operators
    stack = []

    # List to hold the output expression in postfix form
    output = []

    # Process each token in the infix expression
    for token in tokens:
        if token.isalnum():  # Operand (numbers or variable names like a, b, c)
            output.append(token)
        elif token == '(':  # Left parenthesis is always pushed to the stack
            stack.append(token)
        elif token == ')':
            # Pop from the stack to the output until '(' is encountered
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Discard the '(' from the stack
        else:
            # The token is an operator
            # While the stack is not empty and the top of the stack is not '('
            # and precedence of the top is >= current operator, pop from stack to output
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            # Push the current operator onto the stack
            stack.append(token)

    # Pop any remaining operators from the stack to output
    while stack:
        output.append(stack.pop())

    return output


# ✅ Test cases
# Test 1: Simple addition
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # ➕ Simple operation

# Test 2: Operator precedence
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # 🧠 Precedence test

# Test 3: Parentheses override precedence
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # 🧮 Parentheses

# Test 4: Complex expression
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '+', '4', '/', '(', '5', '-', '6', ')', ')']) ==
      ['1', '2', '+', '3', '4', '5', '6', '-', '/', '+', '*'])  # 🔁 Complex

# Test 5: Multiple operators
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '-', 'd', '/', 'e']) ==
      ['a', 'b', 'c', '*', '+', 'd', 'e', '/', '-'])  # 🧮 Variables and precedence
