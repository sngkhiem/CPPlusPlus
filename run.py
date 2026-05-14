import sys, os
import subprocess
import unittest
from antlr4 import *


# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = './antlr/antlr4-4.9.2-complete.jar'
CPL_Dest = 'CompiledFiles'
SRC = './grammar/CPPP.g4'
TESTS = os.path.join(DIR, './tests')


def printUsage():
    print('python run.py gen')
    print('python run.py test <file.CPPP>')


def printBreak():
    print('-----------------------------------------------')


def generateAntlr2Python():
    #print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-Xexact-output-dir', '-o', CPL_Dest, '-no-listener', '-visitor','-Dlanguage=Python3', SRC])
    #print('Generate successfully')

def printStage(stage, message):
    print(f"[Stage {stage}] {message}")

def runCode(astTree, context=None):    
    from semantic.CodeRunner import CodeRunner
    code_runner = CodeRunner()
    astTree.accept(code_runner)

def validate(inputFile):
    if not inputFile.lower().endswith('.cppp'):
        print(f"Only .CPPP files are accepted ({inputFile})")
        exit(1)

    if not os.path.isabs(inputFile):
        inputFile = os.path.join(DIR, inputFile)

    if not os.path.isfile(inputFile):
        print(f"Input rejected: file not found ({inputFile})")
        exit(1)

    return inputFile

def parse(inputFile):
    from CompiledFiles.CPPPLexer import CPPPLexer
    from CompiledFiles.CPPPParser import CPPPParser
    from antlr4.error.ErrorListener import ErrorListener

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected at line {line}:{column}: {msg}")
            exit(1)
    
    lexer = CPPPLexer(FileStream(inputFile))
    token_stream = CommonTokenStream(lexer)
    parser = CPPPParser(token_stream)   
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())    
    return parser.program()

def runTest(inputFile):
    from semantic.ASTGeneration import ASTGeneration
    from semantic.varCheck import varCheck, varError

    inputFile = validate(inputFile)

    tree = parse(inputFile)

    ast_generator = ASTGeneration()
    asttree = tree.accept(ast_generator) 

    check = varCheck()
    try:
        check.check(asttree)
    except varError as e:
        print(e)
        exit(1)   

    runCode(asttree) 

def main(argv):
    #print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    #print('Length of arguments      :  ' + str(len(argv)))    
    #printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    elif argv[0] == 'test':
        if len(argv) < 2:
            printUsage()
            exit(1)
        runTest(argv[1])
    else:
        printUsage()


if __name__ == '__main__':
    main(sys.argv[1:])     
    
    
