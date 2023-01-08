import ply.yacc as yacc
import sys

import difflib
import random as rd
import math

from lex2 import tokens


def p_Programa_Empty(p):
    '''
    Programa : Corpo
    '''
    parser.assembly = f'{p[1]}'


def p_Corpo(p):
    '''
    Corpo : Corpo
          | Decls
          | Proc
    '''
    p[0] = p[1]


def p_Corpo_Rec(p):
    '''
    Corpo : Decls Corpo
          | Proc Corpo
    '''
    p[0] = f"{p[1]}{p[2]}"


def p_Decls(p):
    "Decls : Decl"
    p[0] = f'{p[1]}'


def p_expr(p):
    "expr : INT"
    p[0] = f"PUSHI {int(p[1])}\n"


def p_expr_var(p):
    "expr : ID"
    varName = p[1]
    if varName in parser.variaveis:
        value = parser.variaveis[varName][0]
        p[0] = value


def p_expr_arit(p):
    '''
    expr : exprArit
         | exprRel
    '''
    p[0] = p[1]


def p_Proc_Atrib(p):
    "Proc :  Atrib"
    p[0] = p[1]


# Declaração de uma variavel sem valor
def p_Decl(p):
    "Decl : VAR ID"
    print("a")
    varName = p[2]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = (None, parser.stackPointer)
        p[0] = "PUSHI 0\n"
        parser.stackPointer += 1
    else:
        parser.exito = False
        parser.errorCode = f"Variável com o nome {varName} já existe"


# Declaração de uma variável com atribuição de um valor
def p_Atrib_expr(p):
    "Atrib : VAR ID COM expr"
    varName = p[2]
    if varName not in parser.variaveis:
        value = p[4]
        parser.variaveis[varName] = (value, parser.stackPointer)
        p[0] = f"{value}STOREG {parser.stackPointer}\n"
        parser.stackPointer += 1
    else:
        parser.exito = False
        parser.errorCode = f"Variável com o nome {varName} já existe"


# Cria uma lista sem tamanho
def p_Decl_Lista_NoSize(p):
    "Decl : LISTA ID"
    listName = p[2]
    if listName not in parser.variaveis:
        parser.variaveis[listName] = ([], parser.stackPointer)
        p[0] = f"PUSHN 0\n"
        parser.stackPointer += 1
    else:
        parser.error = (
            f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Cria uma lista com tamanho
def p_DeclLista_Size(p):
    "Decl : LISTA ID INT"
    listName = p[2]
    size = int(p[3])
    if listName not in parser.variaveis:
        parser.variaveis[listName] = (None, parser.stackPointer)
        p[0] = f"PUSHN {size}\n"
        parser.stackPointer += size
    else:
        parser.error = (
            f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Cria uma lista com os valores pretendidos
def p_DeclLista_lista(p):
    "Decl : LISTA ID COM lista"
    lista = p[4]
    numElems = lista.count("PUSHI")
    varName = p[2]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = (lista, parser.stackPointer)
        parser.stackPointer += numElems


# Elementos da lista
def p_lista(p):
    "lista : ABREPR elems FECHAPR"
    p[0] = p[2]


def p_elems(p):
    "elems : INT"
    p[0] = f"PUSHI {p[1]}"


def p_elems_rec(p):
    "elems : INT VIRG elems"
    p[0] = f"PUSHI {p[1]}\n{p[3]}"


# Atribui valores a uma lista de tamanho n
def p_atrib_Lista(p):
    "Atrib : ALTERNA ID ABREPR expr FECHAPR COM expr"
    listName = p[2]
    if listName in parser.variaveis:
        p[0] = f'PUSHGP\nPUSHI {parser.variaveis[listName][1]}\nPADD\n{p[4]}{p[7]}STOREN\n'
    else:
        parser.error = (
            f"Lista com o nome {listName} não definida anteriormente."
        )
        parser.exito = False


# Altera valor de uma variavel existente
def p_alterna_var(p):
    '''Atrib : ALTERNA ID COM expr'''
    varName = p[2]
    if varName in parser.variaveis:
        parser.variaveis[varName] = (p[4], parser.variaveis[varName][1])
        p[0] = f"{p[4]}STOREG {parser.variaveis[varName][1]}\n"


# Expressão Aritmética Soma
def p_soma(p):
    "exprArit : expr SOMA expr"
    p[0] = f"{p[1]}{p[3]}ADD\n"


# Expressão Aritmética Subtração
def p_sub(p):
    "exprArit : expr MENUS expr"
    p[0] = f"{p[1]}{p[3]}SUB\n"


# Expressão Aritmética Multiplicação
def p_mult(p):
    "exprArit : expr SOMANBEZES expr"
    p[0] = f"{p[1]}{p[3]}MUL\n"


# Expressão Aritmética Divisão
def p_div(p):
    "exprArit : expr DIBIDE expr"
    p[0] = f"{p[1]}{p[3]}MUL\n"


# Expressão Aritmética Resto da divisão
def p_rem(p):
    "exprArit : expr SOBRAS expr"
    p[0] = f"{p[1]}{p[3]}MOD\n"


# Expressão Relativa Não
def p_not(p):
    "exprRel : NOUM ABREPC expr FECHAPC"
    p[0] = f"{p[3]}NOT\n"


# Expressão Relativa Igual
def p_gemeo(p):
    "exprRel : GEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}EQUAL\n"


# Expressão Relativa Diferente
def p_naogemeo(p):
    "exprRel : NAOGEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}NOT\nEQUAL\n"


# Expressão Relativa Menor
def p_inf(p):
    "exprRel : MAISPIQUENO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}INF\n"


# Expressão Relativa Menor ou Igual
def p_infeq(p):
    "exprRel : MAISPIQUENOOUGEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}INFEQ\n"


# Expressão Relativa Maior
def p_sup(p):
    "exprRel : MAISGRANDE ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}SUP\n"


# Expressão Relativa Maior ou Igual
def p_supeq(p):
    "exprRel : MAISGRANDEOUGEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}SUPEQ\n"


# Expressão Relativa E
def p_ie(p):
    "exprRel : expr IE expr"
    p[0] = f"{p[1]}{p[3]}ADD\nPUSHI 2\nEQUAL\n"


# Expressão Relativa OU
def p_oue(p):
    "exprRel : expr OUE expr"
    p[0] = f"{p[1]}{p[3]}ADD\nPUSHI 1\nSUPEQ\n"


# Controlo de fluxo (if)
def p_Proc_If(p):
    "Proc : if"
    p[0] = p[1]


# Ciclo (while)
def p_Proc_While(p):
    "Proc : while"
    p[0] = p[1]


# Controlo de fluxo (if then)
def p_if_Then(p):
    "if : SE exprRel LOGO Corpo FIM"
    p[0] = f"{p[2]}JZ l{parser.labels}\n{p[4]}l{parser.labels}: NOP\n"
    parser.labels += 1


# Controlo de fluxo (if then else)
def p_if_Then_Else(p):
    "if : SE exprRel LOGO Corpo SENAO Corpo FIM"
    p[0] = f"{p[2]}JZ l{parser.labels}\n{p[4]}JUMP l{parser.labels}f\nl{parser.labels}: NOP\n{p[6]}l{parser.labels}f: NOP\n"
    parser.labels += 1


# Ciclo (while)
def p_while(p):
    "while : ENQUANTO exprRel FAZ Corpo FIM"
    p[0] = f'l{parser.labels}c: NOP\n{p[2]}JZ l{parser.labels}f\n{p[4]}JUMP l{parser.labels}c\nl{parser.labels}f: NOP\n'
    parser.labels += 1


# ----------------------------------------

def p_error(p):
    print('Syntax error: ', p)
    parser.success = False

# ----------------------------------------


parser = yacc.yacc()
parser.exito = True
parser.errorCode = ""
parser.assembly = ""
parser.variaveis = {}
parser.stackPointer = 0
parser.linhaDeCodigo = 0
parser.labels = 0

assembly = ""

line = input(">")
while line:
    parser.exito = True
    parser.parse(line)
    print(parser.linhaDeCodigo)
    if parser.exito:
        print("--------------------------------------")
        print(f"Variáveis: {parser.variaveis}")
        parser.linhaDeCodigo += 1
        print(parser.assembly)
        assembly += parser.assembly
        print("--------------------------------------")
    else:
        print("--------------------------------------")
        print(parser.errorCode)
        print("--------------------------------------")
        break
    line = input(">")

print(assembly)
