import os
from typing import List, Optional

from .ASTUtils import *
from .ContextUtils import ContextBuildError, RunnerContext, VariableRecord
from .GenerationVisitorInterface import GenerationVisitorInterface


class ContextGeneration(GenerationVisitorInterface):
    VALID_OPTIONS_BY_TYPE = {
        "primitive": [],
        "array": ["distinct"],
        "tree": [],
        "graph": [],
    }

    def __init__(self, base_dir: Optional[str] = None):
        self.base_dir = base_dir or os.getcwd()
        self.errors: List[str] = []
        self.context = RunnerContext()
        self.current_block = ""
        self.current_subtask = ""

    def build(self, ast: Prog) -> RunnerContext:
        self.errors = []
        self.context = RunnerContext()
        self.current_block = ""
        self.current_subtask = ""

        ast.accept(self)

        if self.errors:
            raise ContextBuildError(self.errors)
        return self.context

    def visitProgram(self, node: Prog):
        self._check_unique_subtask_names(node.subtasks)
        subtasks = [subtask.accept(self) for subtask in node.subtasks]
        return self.context

    def visitSubtaskBlock(self, node: Subtask):
        name = self.visitSubtaskName(node.name)
        self.current_subtask = name
        config = node.config.accept(self)
        gen = self._visitBlock("generate", node.generate)
        if node.checker:
            checker = self._visitBlock("checker", node.checker)
        else:
            checker = None
        self.current_subtask = ""
        return Subtask(name, config, gen, checker)

    def visitSubtaskName(self, node: str):
        if not node:
            self._error("subtask name cannot be empty")
        return node

    def visitConfigBlock(self, node: Config):
        input_file = self._strip_quotes(node.input)
        output_file = self._strip_quotes(node.output)

        self._check_file(input_file, ".cppp", "input")
        self._check_file(output_file, ".cpp", "output")

        if self.context.input_file and self.context.input_file != input_file:
            self._error("multiple different input files are not supported in one context")
        if self.context.output_file and self.context.output_file != output_file:
            self._error("multiple different output files are not supported in one context")

        self.context.input_file = input_file
        self.context.output_file = output_file
        return Config(input_file, output_file)

    def visitGenBlock(self, node: Generate):
        stmts = [self.visitFunc(stmt) for stmt in node.stmts]
        return Generate(stmts)

    def visitCheckerBlock(self, node: Checker):
        checks = [self.visitCheck(stmt) for stmt in node.stmts]
        return Checker(checks)

    def visitFunc(self, node: Stmt):
        return node.accept(self)

    def visitVar(self, node: Var):
        self.visitDataType(node.varType)

        for size in node.arraySizes:
            self.visitExpr(size)

        self._check_array_size_usage(node)
        self._check_options(node)
        self._declare(
            VariableRecord(
                name=node.name,
                varType=node.varType,
                value=self._create_value(node.varType),
                block=self.current_block,
                options=list(node.options),
            )
        )

    def visitPrintStmt(self, node: Print):
        for expr in node.exprs:
            self.visitExpr(expr)

    def visitLoopStmt(self, node: Loop):
        self.visitExpr(node.cnt)
        for stmt in node.stmts:
            self.visitFunc(stmt)

    def visitCheck(self, node: check):
        return node.accept(self)

    def visitAssert(self, node: Assert):
        self.visitExpr(node.condition)

    def visitCheckRead(self, node: CheckRead):
        self.visitDataType(node.varType)
        self._declare(
            VariableRecord(
                name=node.name,
                varType=node.varType,
                value=self._create_value(node.varType),
                block=self.current_block,
                source=node.src,
            )
        )

    def visitDataType(self, node: Type):
        if isinstance(node, PrimitiveType):
            return self.visitPrimitiveType(node)
        if isinstance(node, ArrayType):
            return self.visitArrayType(node)
        if isinstance(node, TreeType):
            return self.visitTreeType(node)
        if isinstance(node, GraphType):
            return self.visitGraphType(node)
        self._error(f"unknown data type '{node}'")

    def visitPrimitiveType(self, node: PrimitiveType):
        return self._visitLeaf(node)

    def visitArrayType(self, node: ArrayType):
        self.visitDataType(node.inner)

    def visitTreeType(self, node: TreeType):
        self.visitExpr(node.size)

    def visitGraphType(self, node: GraphType):
        self.visitExpr(node.nodes)
        self.visitExpr(node.edges)

    def visitExpr(self, node: Expr):
        if isinstance(node, Id):
            return self.visitId(node)
        if isinstance(node, Int):
            return self.visitIntLit(node)
        if isinstance(node, Str):
            return self.visitStrLit(node)
        if isinstance(node, BinOp):
            return self.visitBinaryOp(node)
        self._error(f"unknown expression '{node}'")

    def visitId(self, node: Id):
        record = self.context.variables.get(node.name)
        if not record:
            self._error(f"variable '{node.name}' is used before it is declared")
        elif record.block != self.current_block:
            self._error(
                f"variable '{node.name}' was declared in {record.block} block "
                f"and cannot be used in {self.current_block} block"
            )

    def visitIntLit(self, node: Int):
        return self._visitLeaf(node)

    def visitStrLit(self, node: Str):
        return self._visitLeaf(node)

    def visitBinaryOp(self, node: BinOp):
        self.visitExpr(node.left)
        self.visitExpr(node.right)

    def _check_unique_subtask_names(self, subtasks):
        seen_subtasks = set()
        for subtask in subtasks:
            if subtask.name in seen_subtasks:
                self._error(f"duplicate subtask '{subtask.name}'")
            seen_subtasks.add(subtask.name)

    def _visitBlock(self, block_name: str, node):
        previous_block = self.current_block
        self.current_block = block_name
        result = node.accept(self)
        self.current_block = previous_block
        return result

    def _declare(self, record: VariableRecord):
        if record.name in self.context.variables:
            previous = self.context.variables[record.name]
            self._error(
                f"variable '{record.name}' is declared more than once "
                f"(already declared in {previous.block} block)"
            )
            return
        self.context.variables[record.name] = record

    def _check_array_size_usage(self, node: Var):
        if isinstance(node.varType, ArrayType) and not node.arraySizes:
            self._error(f"array variable '{node.name}' must have at least one size")
        elif not isinstance(node.varType, ArrayType) and node.arraySizes:
            self._error(f"only array variables can have sizes: '{node.name}'")

    def _check_options(self, node: Var):
        valid_options = self._valid_options(node)
        if len(node.options) > 1:
            self._error(f"variable '{node.name}' can only have one option")
            return

        for option in node.options:
            checked_option = self.visitOption(option)
            if checked_option not in valid_options:
                self._error(f"invalid option '{checked_option}' for variable '{node.name}'")

    def _valid_options(self, node: Var):
        return set(self.VALID_OPTIONS_BY_TYPE.get(self._type_kind(node.varType), []))

    def visitOption(self, node: str):
        if not node:
            self._error("option cannot be empty")
        return node

    def _type_kind(self, var_type: Type):
        if isinstance(var_type, ArrayType):
            return "array"
        if isinstance(var_type, TreeType):
            return "tree"
        if isinstance(var_type, GraphType):
            return "graph"
        return "primitive"

    def _create_value(self, var_type: Type):
        if isinstance(var_type, PrimitiveType):
            return self._primitive_default(var_type.name)
        if isinstance(var_type, ArrayType):
            return []
        if isinstance(var_type, TreeType):
            return []
        if isinstance(var_type, GraphType):
            return []
        raise TypeError(f"Unsupported variable type: {var_type}")

    def _primitive_default(self, name: str):
        if name in {"int", "ll"}:
            return 0
        if name in {"float", "double"}:
            return 0.0
        if name in {"char", "string"}:
            return ""
        raise TypeError(f"Unsupported primitive type: {name}")

    def _visitLeaf(self, node):
        return node

    def _check_file(self, path: str, extension: str, label: str):
        if not path:
            self._error(f"config {label} file is empty")
            return

        if not path.endswith(extension):
            self._error(f"config {label} file must end with {extension}: {path}")

        full_path = self._resolve_path(path)
        if not os.path.isfile(full_path):
            self._error(f"config {label} file does not exist: {path}")

    def _resolve_path(self, path: str) -> str:
        if os.path.isabs(path):
            return path
        return os.path.join(self.base_dir, path)

    def _strip_quotes(self, value: str) -> str:
        if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
            return value[1:-1]
        return value

    def _error(self, message: str):
        if self.current_subtask:
            self.errors.append(f"{self.current_subtask}: {message}")
        else:
            self.errors.append(message)
