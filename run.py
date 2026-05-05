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
    print('python run.py test')


def printBreak():
    print('-----------------------------------------------')


def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-Xexact-output-dir', '-o', CPL_Dest, '-no-listener', '-visitor','-Dlanguage=Python3', SRC])
    print('Generate successfully')

def runCode(astTree, context=None):    
    from semantic.CodeRunner import CodeRunner
    code_runner = CodeRunner()
    astTree.accept(code_runner)


def runTest():
    #print('Running testcases...')
       
    from CompiledFiles.CPPPLexer import CPPPLexer
    from CompiledFiles.CPPPParser import CPPPParser
    from antlr4.error.ErrorListener import ErrorListener

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg}")
            exit(1)  # Exit the program with an error

    filename = 'testcase.txt'
    inputFile = os.path.join(DIR, './tests', filename)    
    
    # Reset the input stream for parsing and catch the error
    lexer = CPPPLexer(FileStream(inputFile))
    token_stream = CommonTokenStream(lexer)

    parser = CPPPParser(token_stream)   
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())    
    try:
        parser.program()
        print("Input accepted")
    except SystemExit:        
        pass
    
    printBreak()
    #print('Run tests completely')
    
    input_stream = FileStream(inputFile)
    lexer = CPPPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CPPPParser(stream)
    tree = parser.program()  
    #print('Parser tree: ', tree.toStringTree(recog=parser)) 
    

    from semantic.ASTGeneration import ASTGeneration
    from semantic.varCheck import varCheck, varError
    ast_generator = ASTGeneration()
    asttree = tree.accept(ast_generator) 
    #print('this is asttree:', asttree)
    check = varCheck()
    try:
        check.check(asttree)
    except varError as e:
        print(e)
        exit(1)   

    runCode(asttree) 

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    elif argv[0] == 'test':       
        runTest()
    else:
        printUsage()


if __name__ == '__main__':
    main(sys.argv[1:])     
    
    
