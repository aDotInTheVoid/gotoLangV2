class NodeVisitor(object):
    """Parent class for classes looking at nodes."""

    def visit(self, node):
        """Input node, call visit function for that paticlar node type."""
        method_name = 'visit_' + type(node).__name__.lower()
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Raise error if no visit method exists for node type."""
        raise Exception('No visit_{} method'.format(type(node.__name__)))



class Interpriter(NodeVisitor):
    """Inputs AST, returns integer that that ast evaluates to."""

    def __init__(self):
        """Save the variables."""
        self.global_scope = dict()

    def visit_assign(self, node):
        var_name = node.left.value
        self.global_scope[var_name] = self.visit(node.right)

    def visit_input(self, node):
        value = input()

        try:
            value = float(value)
        except ValueError:
            pass

        self.global_scope[node.var.value] = value

    def visit_output(self, node):
        print(self.visit(node.expr))

    def visit_goto(self, node):
        return self.visit(node.expr)


    def visit_binop(self, node):
        """Visit and evaluate a BinOP Node."""
        try:
            if node.op == '+':
                return self.visit(node.left) + self.visit(node.right)
            elif node.op == '-':
                return self.visit(node.left) - self.visit(node.right)
            elif node.op == '*':
                return self.visit(node.left) * self.visit(node.right)
            elif node.op == '/':
                return self.visit(node.left) / self.visit(node.right)
            elif node.op == '%':
                return self.visit(node.left) % self.visit(node.right)
            elif node.op == '^':
                return self.visit(node.left) ** self.visit(node.right)
        except (ZeroDivisionError, TypeError) as e:
            print("Error: unsupported operand type(s) for -: 'int' and 'str'")
            exit()

    def visit_unaryop(self, node):
        """Visit and evaluate a UnaryOp."""
        op = node.op
        if op == "+":
            return self.visit(node.expr)
        else:
            return -self.visit(node.expr)


    def visit_num(self, node):
        """Return a numbers value."""
        return node.value

    def visit_var(self, node):
        var_name = node.value
        val = self.global_scope.get(var_name)
        if val is None:
            raise NameError(repr(var_name))
        else:
            return val

    def visit_string(self, node):
        return node.value

    def visit_noop(self, node):
        pass

    def visit_var(self, node):
        var_name = node.value
        val = self.global_scope.get(var_name)
        if val is None:
            raise NameError(repr(var_name))
        else:
            return val
