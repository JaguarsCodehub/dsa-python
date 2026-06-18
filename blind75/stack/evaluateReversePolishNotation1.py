# Evaluate Reverse Polish Notation
class Solution(object):
    def resolves(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return int(float(a) / b)
        
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:

                b = stack.pop()
                a = stack.pop()
                operator = token
                stack.append(self.resolves(a, b, operator))

            else:
                stack.append(int(token))

        return stack[-1]