from semantic.ASTUtils import *

class varError(Exception):
    pass

class varCheck:
    def __init__(self):
        self.vars = set()
        self.errors = []

    def check(self, ast):
        self.vars = set()
        self.errors = []
        self.dfs(ast)

        if self.errors:
            raise varError("\n".join(self.errors))
    
    def dfs(self, node):
        if isinstance(node, Prog):
            for subtask in node.subtasks:
                self.dfs(subtask)
        elif isinstance(node, Subtask):
            self.vars = set()
            self.dfs(node.generate)
            if node.checker:
                self.dfs(node.checker)
        elif isinstance(node, Generate) or isinstance(node, Checker):
            for stmt in node.stmts:
                self.dfs(stmt)
        elif isinstance(node, Var):
            for dim in node.dims:
                self.dfs(dim)
            if node.name in self.vars:
                self.errors.append(f"'{node.name}' is already defined.")
            else:
                self.vars.add(node.name)
        elif isinstance(node, CheckRead):
            if node.name in self.vars:
                self.errors.append(f"'{node.name}' is already defined.")
            else: 
                self.vars.add(node.name)
        elif isinstance(node, Print):
            for expr in node.exprs:
                self.dfs(expr)
        elif isinstance(node, Loop):
            self.dfs(node.cnt)
            for stmt in node.stmts:
                self.dfs(stmt)
        elif isinstance(node, Assert):
            self.dfs(node.condition)
        elif isinstance(node, BinOp):
            self.dfs(node.left)
            self.dfs(node.right)
        elif isinstance(node, Id):
            if node.name not in self.vars:
                self.errors.append(f"'{node.name}' is not define.")
