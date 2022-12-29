import ply.yacc as yacc
import sys

import difflib
import random as rd
import math

from lex2 import tokens


def p_programa(p):
    '''
    programa : comentario
             | variavel
             | Expr
             | Busca
    '''

def p_comentario(p):
    "comentario : COMENTARIO ABREPC STRING FECHAPC"
    parser.numeroComents += 1


def p_variavel(p):
    '''
    variavel : Decl
             | alteraVar

    '''
    p[0] = p[1]


# Criar varável sem valor
def p_Decl_NoAssign(p):
    '''
    Decl : VAR ID
    '''
    varName = p[2]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = None
        parser.vars += 1
    else:
        print(f"Variável {varName} já definida.")
        parser.exito = False


# Criar variável com valor INT
def p_Decl_Int(p):
    '''
    Decl : VAR ID COM INT
    '''
    varName = p[2]
    value = int(p[4])
    if varName not in parser.variaveis:
        parser.variaveis[varName] = value
        parser.vars += 1
    else:
        print(f"Variável {varName} já definida.")
        parser.exito = False



# Criar variável com valor de outra var
def p_Decl_Var(p):
    '''
    Decl : VAR ID COM ID
    '''
    varName = p[2]
    varValue = p[4]
    if varName not in parser.variaveis:
        if varValue in parser.variaveis:
            parser.variaveis[varName] = parser.variaveis[varValue]
            parser.vars += 1
        else:
            print(f"Variável {varValue} não definida anteriormente")
            parser.exito=False

    else:
        print(f"Variável {varName} já definida.")
        parser.exito = False


# Criar variável com valor de uma expressão
def p_Decl_Expr(p):
    '''
    Decl : VAR ID COM Expr
    '''
    varName = p[2]
    varValue = p[4]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = varValue
        parser.vars += 1
    else:
        print(f"Variável {varName} já definida.")
        parser.exito = False

# Altera o valor de uma variável para um INT
def p_alteraVar_Int(p):
    '''
    alteraVar : ALTERNA ID COM INT
    '''
    varName = p[2]
    value = p[4]
    if varName in parser.variaveis:
        parser.variaveis[varName] = int(value)
    else:
        print(f"Variável {varName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma variável para o resultado de uma expressao
def p_alteraVar_expr(p):
    '''
    alteraVar : ALTERNA ID COM Expr
    '''
    varName = p[2]
    value = p[4]
    if varName in parser.variaveis:
        parser.variaveis[varName] = int(value)
    else:
        print(f"Variável {varName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma variável com outra variavel
def p_alteraVar_Var(p):
    '''
    alteraVar : ALTERNA ID COM ID
    '''
    varName = p[2]
    varValue = p[4]
    if varName in parser.variaveis:
        if varValue in parser.variaveis:
            parser.variaveis[varName] = parser.variaveis[varValue]
        else:
            print(f"Variavel {varValue} não definida anteriormente")
            parser.exito=False
    else:
        print(f"Variável {varName} não definida anteriormente.")
        parser.exito = False


# -------


# Altera o valor de uma lista numa dada posicao pelo de um inteiro
def p_alteraLista_Int(p):
    '''
    alteraVar : ALTERNA ID INT COM INT
    '''
    arrayName = p[2]
    indexForReplacement = int(p[3])
    valueForReplacement = int(p[5])
    if arrayName in parser.variaveis:
        if indexForReplacement<len(parser.variaveis[arrayName]):
            parser.variaveis[arrayName][indexForReplacement] = valueForReplacement
        else:
            print(f"Indice fora de alcance")
            parser.exito = False
    else:
        print(f"Variável {arrayName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma lista numa dada posicao pelo de uma expressao aritmetica
def p_alteraLista_expr(p):
    '''
    alteraVar : ALTERNA ID INT COM Expr
    '''
    arrayName = p[2]
    indexForReplacement = int(p[3])
    valueForReplacement = int(p[5])
    if arrayName in parser.variaveis:
        if indexForReplacement<len(parser.variaveis[arrayName]):
            parser.variaveis[arrayName][indexForReplacement] = valueForReplacement
        else:
            print(f"Indice fora de alcance")
            parser.exito = False
    else:
        print(f"Variável {arrayName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma lista numa dada posicao pelo de outra
def p_alteraLista_Var(p):
    '''
    alteraVar : ALTERNA ID INT COM ID
    '''
    arrayName = p[2]
    indexForReplacement = int(p[3])
    valueForReplacement = p[5]
    if arrayName in parser.variaveis:
        if valueForReplacement in parser.variaveis:
            if indexForReplacement<len(parser.variaveis[arrayName]):
                parser.variaveis[arrayName][indexForReplacement]= parser.variaveis[valueForReplacement]
            else:
                print(f"Indice fora de alcance")
                parser.exito = False
        else:
            print(f"Variável {valueForReplacement} não definida anteriormente.")
            parser.exito = False
    else:
        print(f"Variável {arrayName} não definida anteriormente.")
        parser.exito = False



def p_ExpressaoAritmetica(p):
    '''
    Expr : soma
         | sub
         | mult
         | div
         | exp
         | resto
    '''
    p[0] = p[1]


# Soma
def p_soma(p):
    '''
    soma : INT SOMA INT
    '''
    p[0] = int(p[1]) + int(p[3])


# Soma
def p_soma_id(p):
    '''
    soma : INT SOMA ID
    '''
    varName = p[3]
    if varName in parser.variaveis:
        if parser.variaveis[varName]!=None:
            p[0] = int(p[1]) + parser.variaveis[varName]
        else:
            print(f"Operação impossível: INT + NoneType{varName}")
            parser.exito=False
    else:
        print(f"Variável {varName} não definida anteriormente")
        parser.exito = False


# Subtração
def p_sub(p):
    '''
    sub : INT MENUS INT
    '''
    p[0] = int(p[1]) - int(p[3])


# Subtracao
def p_sub_id(p):
    '''
    sub : INT MENUS ID
    '''
    varName = p[3]
    if varName in parser.variaveis:
        if parser.variaveis[varName]!=None:
            p[0] = int(p[1]) - parser.variaveis[varName]
        else:
            print(f"Operação impossível: INT - NoneType{varName}")
            parser.exito=False
    else:
        print(f"Variável {varName} não definida anteriormente")
        parser.exito = False


# Multiplicação
def p_mult(p):
    '''
    mult : INT SOMANBEZES INT
    '''
    p[0] = int(p[1]) * int(p[3])


# Multiplicação
def p_mult_id(p):
    '''
    mult : INT SOMANBEZES ID
    '''
    varName = p[3]
    if varName in parser.variaveis:
        if parser.variaveis[varName]!=None:
            p[0] = int(p[1]) * parser.variaveis[varName]
        else:
            print(f"Operação impossível: INT * NoneType{varName}")
            parser.exito=False
    else:
        print(f"Variável {varName} não definida anteriormente")
        parser.exito = False


# Divisão
def p_div(p):
    '''
    div : INT DIBIDE INT
    '''
    p[0] = int(p[1]) / int(p[3])


# Divisao
def p_div_id(p):
    '''
    div : INT DIBIDE ID
    '''
    varName = p[3]
    if varName in parser.variaveis:
        if parser.variaveis[varName]!=None:
            p[0] = int(p[1]) / parser.variaveis[varName]
        else:
            print(f"Operação impossível: INT / NoneType{varName}")
            parser.exito=False
    else:
        print(f"Variável {varName} não definida anteriormente")
        parser.exito = False


# Exponenciação
def p_exp(p):
    '''
    exp : INT CHAPEU INT
    '''
    p[0] = int(math.pow(int(p[1]),int(p[3])))


# Exponenciação
def p_exp_id(p):
    '''
    exp : INT CHAPEU ID
    '''
    varName = p[3]
    if varName in parser.variaveis:
        if parser.variaveis[varName]!=None:
            p[0] = int(math.pow(int(p[1]),parser.variaveis[varName]))
        else:
            print(f"Operação impossível: INT ^ NoneType{varName}")
            parser.exito=False
    else:
        print(f"Variável {varName} não definida anteriormente")
        parser.exito = False


# Resto da divisão
def p_resto(p):
    '''
    resto : INT SOBRAS INT
    '''
    p[0] = int(int(p[1]) % int(p[3]))


# Resto
def p_resto_id(p):
    '''
    resto : INT SOBRAS ID
    '''
    varName = p[3]
    if varName in parser.variaveis:
        if parser.variaveis[varName]!=None:
            p[0] = int(int(p[1]) % parser.variaveis[varName])
        else:
            print(f"Operação impossível: INT % NoneType{varName}")
            parser.exito=False
    else:
        print(f"Variável {varName} não definida anteriormente")
        parser.exito = False


# Cria Array sem tamanho
def p_Decl_Lista_NoSize(p):
    '''
    Decl : LISTA ID
    '''
    listName = p[2]
    if listName not in parser.variaveis:
        parser.variaveis[listName] = []
        parser.vars += 1
    else:
        print(f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Cria Array com tamanho
def p_Decl_Lista(p):
    '''
    Decl : LISTA ID INT
    '''
    listName = p[2]
    size = int(p[3])
    if listName not in parser.variaveis:
        parser.variaveis[listName] = [None for i in range(size)]
        parser.vars += 1
    else:
        print(f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Retorna o elemento no indice do array
def p_Busca_Lista(p):
    '''
    Busca : BUSCA ID INT 
    '''
    matrizName = p[2]
    indice1 = int(p[3])
    if isinstance(parser.variaveis[matrizName], int) or parser.variaveis[matrizName]==None:
        print("Operação inválida sobre o tipo de dados")
        parser.exito = False
    elif indice1 < len(parser.variaveis[matrizName]) :
        p[0] = parser.variaveis[matrizName][indice1]
    else:
        print(f"Indice fora de alcance")
        parser.exito = False


# Cria Matriz sem tamanho
def p_Decl_Matriz_NoSize(p):
    '''
    Decl : MATRIZ ID
    '''
    matrizName = p[2]
    if matrizName not in parser.variaveis:
        parser.variaveis[matrizName] = [[]]
        parser.vars += 1
    else:
        print(f"Matriz {matrizName} já definida.")
        parser.exito = False


# Cria Matriz com tamanho
def p_Decl_Matriz(p):
    '''
    Decl : MATRIZ ID INT INT
    '''
    matrizName = p[2]
    size1 = int(p[3])
    size2 = int(p[4])
    if matrizName not in parser.variaveis:
        parser.variaveis[matrizName] = [[None for j in range(size1)] for i in range(size2)]
        parser.vars += 1
    else:
        print(f"Matriz {matrizName} já definida.")
        parser.exito = False


# Retorna o elemento no indice da matriz
def p_Busca_Matriz(p):
    '''
    Busca : BUSCA ID INT INT
    '''
    matrizName = p[2]
    indice1 = int(p[3])
    indice2 = int(p[4])
    if isinstance(parser.variaveis[matrizName], int) or parser.variaveis[matrizName]==None:
        print("Operação inválida sobre o tipo de dados")
        parser.exito = False
    elif indice1 < len(parser.variaveis[matrizName]) and indice2 < len(parser.variaveis[matrizName][indice1]):
        p[0] = parser.variaveis[matrizName][indice1][indice2]
    else:
        print(f"Indice fora de alcance")
        parser.exito = False


def p_error(p):
    print(p)
    try:
        syntatic_sugar(p.value)
        parser.exito = False
    except:
        print(p)
        parser.exito=False


def syntatic_sugar(syntaxError):
    error = syntaxError.upper()
    matches = difflib.get_close_matches(error, tokens, n=2, cutoff=0.6)
    if matches != []:
        parser.error = f"Syntax error na linha {parser.linhaDeCodigo}: Querias dizer {rd.choice(matches)}"


parser = yacc.yacc()

parser.vars = 0
parser.numeroComents = 0
parser.variaveis = {}
parser.linhaDeCodigo = 0
parser.error = "Syntax Error"

for line in sys.stdin:
    parser.exito = True
    parser.parse(line)
    if parser.exito:
        print("--------------------------------------")
        print(f"Variáveis: {parser.variaveis}")
        print("--------------------------------------")
    else:
        print("--------------------------------------")
        print(parser.error)
        print("--------------------------------------")
        break
