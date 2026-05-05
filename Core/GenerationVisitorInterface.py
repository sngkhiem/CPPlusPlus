from abc import ABC, abstractmethod


class GenerationVisitorInterface(ABC):
    @abstractmethod
    def visitProgram(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitSubtaskBlock(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitSubtaskName(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitConfigBlock(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitGenBlock(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitCheckerBlock(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitPrimitiveType(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitDataType(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitFunc(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitVar(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitPrintStmt(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitLoopStmt(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitCheck(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitCheckRead(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitOption(self, node):
        raise NotImplementedError

    @abstractmethod
    def visitExpr(self, node):
        raise NotImplementedError
