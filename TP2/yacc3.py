import ply.yacc as yacc
import sys

import difflib
import random as rd
import math

from lex2 import tokens

def p_Programa_Empty(p):
    "Programa : Decls"
    parser.assembly = f'{p[1]}'

def p_Decls(p):
    "Decls    : Decl"
    p[0] = f'{p[1]}'

def p_Decls_Recursiva(p):
    "Decls    : Decls Decl"
    p[0] = f'{p[1]}{p[2]}'

def p_expr(p):
    "expr : INT"
    p[0] = f"PUSHI {int(p[1])}\n"

def p_expr_var(p):
    "expr : ID"
    varName = p[1]
    if varName in parser.variaveis:
        value = parser.variaveis[varName][0]
        p[0]=value
        

def p_Decl(p):
    "Decl : VAR ID"
    print("a")
    varName = p[2]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = (None, parser.stackPointer)
        p[0] = "PUSHI 0\n"
        parser.stackPointer+=1
    else:
        parser.exito = False
        parser.errorCode = f"Variável com o nome {varName} já existe"

def p_Decl_expr(p):
    "Decl : VAR ID COM expr"
    varName = p[2]
    if varName not in parser.variaveis:
        value = p[4]
        parser.variaveis[varName] = (value, parser.stackPointer)
        print(f"{value}STOREG {parser.stackPointer}\n")
        p[0] = f"{value}STOREG {parser.stackPointer}\n"
        parser.stackPointer+=1
    else:
        parser.exito = False
        parser.errorCode = f"Variável com o nome {varName} já existe"

def p_Decl_Lista(p):
    "Decl :  LISTA ID INT"
    varName = p[2]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = ([],parser.stackPointer)
        p[0] = f"PUSHN {int(p[3])}"
        parser.stackPointer+=1
    else:
        parser.exito = False
        parser.errorCode = f"Variável com o nome {varName} já existe"


def p_soma(p):
    "expr : expr SOMA expr"
    p[0] = f"{p[1]}{p[3]}ADD\n"

def p_sub(p):
    "expr : expr MENUS expr"
    p[0] = f"{p[1]}{p[3]}SUB\n"

def p_mult(p):
    "expr : expr SOMANBEZES expr"
    p[0] = f"{p[1]}{p[3]}MUL\n"

def p_div(p):
    "expr : expr DIBIDE expr"
    p[0] = f"{p[1]}{p[3]}MUL\n"

def p_rem(p):
    "expr : expr SOBRAS expr"
    p[0] = f"{p[1]}{p[3]}MOD\n"

def p_not(p):
    "expr : NOUM ABREPC expr FECHAPC"
    p[0] = f"{p[3]}NOT\n"

def p_inf(p):
    "expr : MAISPIQUENO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}INF\n"

def p_infeq(p):
    "expr : MAISPIQUENOOUGEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}INFEQ\n"

def p_sup(p):
    "expr : MAISGRANDE ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}SUP\n"

def p_supeq(p):
    "expr : MAISGRANDEOUGEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}SUPEQ\n"


#----------------------------------------
def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

#----------------------------------------

parser = yacc.yacc()
parser.exito = True
parser.errorCode = ""
parser.assembly = ""
parser.variaveis = {}
parser.stackPointer = 0
parser.linhaDeCodigo=0

assembly =""

line = input(">")
while line:
    parser.exito = True
    parser.parse(line)
    print(parser.linhaDeCodigo)
    if parser.exito:
        print("--------------------------------------")
        print(f"Variáveis: {parser.variaveis}")
        parser.linhaDeCodigo+=1
        print(parser.assembly)
        assembly+=parser.assembly
        print("--------------------------------------")
    else:
        print("--------------------------------------")
        print(parser.errorCode)
        print("--------------------------------------")
        break
    line = input(">")

print(assembly)
