from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .ASTUtils import Type


class ContextBuildError(Exception):
    def __init__(self, errors: List[str]):
        self.errors = errors
        super().__init__("\n".join(errors))


@dataclass
class VariableRecord:
    name: str
    varType: Type
    value: object
    block: str
    options: List[str] = field(default_factory=list)
    source: Optional[str] = None

    def __str__(self):
        options = f", options={self.options}" if self.options else ""
        source = f", source={self.source}" if self.source else ""
        return (
            f"{self.name}: value={self.value}, type={self.varType}, "
            f"block={self.block}{options}{source}"
        )


@dataclass
class RunnerContext:
    # Shared context produced before CodeRunner starts.
    # `variables` is the single source of truth:
    #   context.variables["N"].value   -> current stored value
    #   context.variables["N"].varType -> DSL type metadata
    #   context.variables["N"].block   -> owning block: generate/checker
    input_file: str = ""
    output_file: str = ""
    variables: Dict[str, VariableRecord] = field(default_factory=dict)

    def __str__(self):
        variables = "\n".join(
            f"  {name} -> {record}" for name, record in self.variables.items()
        )
        if not variables:
            variables = "  <empty>"
        return (
            f"RunnerContext\n"
            f"input_file={self.input_file}\n"
            f"output_file={self.output_file}\n"
            f"variables:\n{variables}"
        )
