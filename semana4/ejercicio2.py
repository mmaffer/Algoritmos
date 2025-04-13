class InfixEvaluator:
    """Class to convert and evaluate infix expressions using stacks."""

    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.right_associative = {'^'}

    def precedence(self, op):
        return self.operators.get(op, 0)

    def is_operator(self, token):
        return token in self.operators

    def to_postfix(self, expression):
        """Convert infix to postfix without using regex."""
        output = []
        stack = []
        i = 0

        while i < len(expression):
            char = expression[i]

            if char.isspace():
                i += 1
                continue

            if char.isdigit() or char == '.':
                num = []
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num.append(expression[i])
                    i += 1
                output.append(''.join(num))
                continue

            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove '('
            elif self.is_operator(char):
                while (stack and stack[-1] != '(' and
                        (self.precedence(stack[-1]) > self.precedence(char) or
                        (self.precedence(stack[-1]) == self.precedence(char) 
                            and char not in self.right_associative))):
                    output.append(stack.pop())
                stack.append(char)

            i += 1

        while stack:
            output.append(stack.pop())

        return ' '.join(output)

    def evaluate_postfix(self, expression):
        """Evaluate a postfix expression."""
        stack = []
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '^': lambda a, b: a ** b
        }

        for token in expression.split():
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(float(token))

        return stack[0]

evaluator = InfixEvaluator()

test_cases = {
    "1 + 2 * 3": 7.0,
    "(1 + 2) * (3 + 4)": 21.0,
    "3 + 4 * 2 / (1 - 5) ^ 2": 3.5
}

for expr, expected in test_cases.items():
    postfix = evaluator.to_postfix(expr)
    result = evaluator.evaluate_postfix(postfix)
    passed = abs(result - expected) < 1e-6
    print(f"Infix Expression: {expr}")
    print(f"Postfix: {postfix}")
    print(f"Result: {result}")
    print(f"Test Passed: {'Yes' if passed else 'No'}")
    print("-" * 40)
