import ply.yacc as yacc
import sys

import difflib
import random as rd
import math

from lex2 import tokens


def p_programa(p):
    '''
    programa : acoes
    '''
    p[0]=p[1]

#falta adicionar ciclos
def p_acoes(p):
    '''
    acoes : decl
          | op

    '''
    p[0]=p[1]

def p_decls_rec(p):
    '''
    decls : decls decl
    '''
    p[0]=f"{p[1]}{p[2]}"

def p_decls(p):
    '''
    decls : decl
    '''
    p[0]=p[1]

#tipos de declaracoes
#comentario
#variavel
#array
#lista

def p_decl_comentario(p):
    "decl : COMENTARIO ABREPC STRING FECHAPC"
    parser.numeroComents += 1


# Criar varável sem valor
def p_decl_NoAssign(p):
    '''
    decl : VAR ID
    '''
    varName = p[2]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = None
        parser.vars += 1
    else:
        parser.error=(f"Variável {varName} já definida.")
        parser.exito = False


# Criar variável com valor INT
def p_decl_Int(p):
    '''
    decl : VAR ID COM INT
    '''
    varName = p[2]
    value = int(p[4])
    if varName not in parser.variaveis:
        parser.variaveis[varName] = value
        parser.vars += 1
    else:
        parser.error=(f"Variável {varName} já definida.")
        parser.exito = False

# Criar variável com valor de outra var
def p_decl_Var(p):
    '''
    decl : VAR ID COM ID
    '''
    varName = p[2]
    varValue = p[4]
    if varName not in parser.variaveis:
        if varValue in parser.variaveis:
            parser.variaveis[varName] = parser.variaveis[varValue]
            parser.vars += 1
        else:
            parser.error = (f"Variável {varValue} não definida anteriormente")
            parser.exito=False

    else:
        parser.error = (f"Variável {varName} já definida.")
        parser.exito = False


# Criar variável com valor de uma expressão
def p_decl_op(p):
    '''
    decl : VAR ID COM op
    '''
    varName = p[2]
    varValue = p[4]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = varValue
        parser.vars += 1
    else:
        parser.error = (f"Variável {varName} já definida.")
        parser.exito = False



# Cria Array sem tamanho
def p_decl_Lista_NoSize(p):
    '''
    decl : LISTA ID
    '''
    listName = p[2]
    if listName not in parser.variaveis:
        parser.variaveis[listName] = []
        parser.vars += 1
    else:
        parser.error = (f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Cria Array com tamanho
def p_decl_Lista(p):
    '''
    decl : LISTA ID INT
    '''
    listName = p[2]
    size = int(p[3])
    if listName not in parser.variaveis:
        parser.variaveis[listName] = [None for i in range(size)]
        parser.vars += 1
    else:
        parser.error = (f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Cria Matriz sem tamanho
def p_decl_Matriz_NoSize(p):
    '''
    decl : MATRIZ ID
    '''
    matrizName = p[2]
    if matrizName not in parser.variaveis:
        parser.variaveis[matrizName] = [[]]
        parser.vars += 1
    else:
        parser.error = (f"Matriz {matrizName} já definida.")
        parser.exito = False


# Cria Matriz com tamanho
def p_decl_Matriz(p):
    '''
    decl : MATRIZ ID INT INT
    '''
    matrizName = p[2]
    size1 = int(p[3])
    size2 = int(p[4])
    if matrizName not in parser.variaveis:
        parser.variaveis[matrizName] = [[None for j in range(size1)] for i in range(size2)]
        parser.vars += 1
    else:
        parser.error = (f"Matriz {matrizName} já definida.")
        parser.exito = False


# Altera o valor de uma variável para um INT
def p_decl_alteraVar_Int(p):
    '''
    decl : ALTERNA ID COM INT
    '''
    varName = p[2]
    value = p[4]
    if varName in parser.variaveis:
        parser.variaveis[varName] = int(value)
    else:
        parser.error = (f"Variável {varName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma variável para o resultado de uma expressao
def p_decl_alteraVar_op(p):
    '''
    decl : ALTERNA ID COM op
    '''
    varName = p[2]
    value = p[4]
    if varName in parser.variaveis:
        parser.variaveis[varName] = int(value)
    else:
        parser.error = (f"Variável {varName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma variável com outra variavel
def p_decl_alteraVar_Var(p):
    '''
    decl : ALTERNA ID COM ID
    '''
    varName = p[2]
    varValue = p[4]
    if varName in parser.variaveis:
        if varValue in parser.variaveis:
            parser.variaveis[varName] = parser.variaveis[varValue]
        else:
            parser.error = (f"Variavel {varValue} não definida anteriormente")
            parser.exito=False
    else:
        parser.error = (f"Variável {varName} não definida anteriormente.")
        parser.exito = False


# -------


# Altera o valor de uma lista numa dada posicao pelo de um inteiro
def p_decl_alteraLista_Int(p):
    '''
    decl : ALTERNA ID INT COM INT
    '''
    arrayName = p[2]
    indexForReplacement = int(p[3])
    valueForReplacement = int(p[5])
    if arrayName in parser.variaveis:
        if indexForReplacement<len(parser.variaveis[arrayName]):
            parser.variaveis[arrayName][indexForReplacement] = valueForReplacement
        else:
            parser.error = (f"Indice fora de alcance")
            parser.exito = False
    else:
        parser.error = (f"Variável {arrayName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma lista numa dada posicao pelo de uma expressao aritmetica
def p_decl_alteraLista_op(p):
    '''
    decl : ALTERNA ID INT COM op
    '''
    arrayName = p[2]
    indexForReplacement = int(p[3])
    valueForReplacement = int(p[5])
    if arrayName in parser.variaveis:
        if indexForReplacement<len(parser.variaveis[arrayName]):
            parser.variaveis[arrayName][indexForReplacement] = valueForReplacement
        else:
            parser.error = (f"Indice fora de alcance")
            parser.exito = False
    else:
        parser.error = (f"Variável {arrayName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma lista numa dada posicao pelo de outra
def p_decl_alteraLista_Var(p):
    '''
    decl : ALTERNA ID INT COM ID
    '''
    arrayName = p[2]
    indexForReplacement = int(p[3])
    valueForReplacement = p[5]
    if arrayName in parser.variaveis:
        if valueForReplacement in parser.variaveis:
            if indexForReplacement<len(parser.variaveis[arrayName]):
                parser.variaveis[arrayName][indexForReplacement]= parser.variaveis[valueForReplacement]
            else:
                parser.error = (f"Indice fora de alcance")
                parser.exito = False
        else:
            parser.error = (f"Variável {valueForReplacement} não definida anteriormente.")
            parser.exito = False
    else:
        parser.error = (f"Variável {arrayName} não definida anteriormente.")
        parser.exito = False


def p_op(p):
    '''
    op : ExprArit
       | ExprRel
       | ExprLog
       | Busca
    '''
    p[0]=p[1]


def p_ExpressaoAritmetica(p):
    '''
    ExprArit : soma
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
            parser.error = (f"Operação impossível: INT + NoneType{varName}")
            parser.exito=False
    else:
        parser.error = (f"Variável {varName} não definida anteriormente")
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
            parser.error = (f"Operação impossível: INT - NoneType{varName}")
            parser.exito=False
    else:
        parser.error = (f"Variável {varName} não definida anteriormente")
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
            parser.error = (f"Operação impossível: INT * NoneType{varName}")
            parser.exito=False
    else:
        parser.error = (f"Variável {varName} não definida anteriormente")
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
            parser.error = (f"Operação impossível: INT / NoneType{varName}")
            parser.exito=False
    else:
        parser.error = (f"Variável {varName} não definida anteriormente")
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
            parser.error = (f"Operação impossível: INT ^ NoneType{varName}")
            parser.exito=False
    else:
        parser.error = (f"Variável {varName} não definida anteriormente")
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
            parser.error = (f"Operação impossível: INT % NoneType{varName}")
            parser.exito=False
    else:
        parser.error = (f"Variável {varName} não definida anteriormente")
        parser.exito = False

#


# Retorna o elemento no indice do array
def p_Busca_Lista(p):
    '''
    Busca : BUSCA ID INT 
    '''
    matrizName = p[2]
    indice1 = int(p[3])
    if isinstance(parser.variaveis[matrizName], int) or parser.variaveis[matrizName]==None:
        parser.error = ("Operação inválida sobre o tipo de dados")
        parser.exito = False
    elif indice1 < len(parser.variaveis[matrizName]) :
        p[0] = parser.variaveis[matrizName][indice1]
    else:
        parser.error = (f"Indice fora de alcance")
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
        parser.error = ("Operação inválida sobre o tipo de dados")
        parser.exito = False
    elif indice1 < len(parser.variaveis[matrizName]) and indice2 < len(parser.variaveis[matrizName][indice1]):
        p[0] = parser.variaveis[matrizName][indice1][indice2]
    else:
        parser.error = (f"Indice fora de alcance")
        parser.exito = False


def p_ExprRel(p):
    '''
    ExprRel : maisGrande
            | maisPiqueno
            | gemeo
            | maisGrandeOuGemeo
            | maisPiquenoOuGemeo
    '''
    p[0] = p[1]

def p_maisGrande(p):
    '''
    maisGrande : MAISGRANDE ABREPC INT VIRG INT FECHAPC
    '''
    p[0] = f"{int(p[3])>int(p[5])}"
    parser.error = (p[0])

def p_maisPiqueno(p):
    '''
    maisPiqueno : MAISPIQUENO ABREPC INT VIRG INT FECHAPC
    '''
    p[0] = f"{int(p[3])<int(p[5])}"
    parser.error = (p[0])

def p_gemeo(p):
    '''
    gemeo : GEMEO ABREPC INT VIRG INT FECHAPC
    '''
    p[0] = f"{int(p[3])==int(p[5])}"
    parser.error = (p[0])

def p_maisGrandeOuGemeo(p):
    '''
    maisGrandeOuGemeo : MAISGRANDEOUGEMEO ABREPC INT VIRG INT FECHAPC
    '''
    p[0] = f"{int(p[3])>=int(p[5])}"
    parser.error = (p[0])

def p_maisPiquenoOuGemeo(p):
    '''
    maisPiquenoOuGemeo : MAISPIQUENOOUGEMEO ABREPC INT VIRG INT FECHAPC
    '''
    p[0] = f"{int(p[3])<=int(p[5])}"
    parser.error = (p[0])


def p_ExprLog(p):
    '''
    ExprLog : ie
            | oue
            | noum
    '''
    p[0]=p[1]

def p_ie(p):
    '''
    ie : INT IE INT
    '''
    p[0]=f"{int(p[1]) and int(p[3])}"
    print(p[0])

def p_ie_1Var(p):
    '''
    ie : INT IE ID
    '''
    var = p[3]
    if var in parser.variaveis: 
        p[0]=f"{int(p[1]) and parser.variaveis[var]}"
        print(p[0])
    else:
        parser.error = (f"Variável {var} não definida")
        parser.exito = False

def p_ie_1Var1(p):
    '''
    ie : ID IE INT
    '''
    var = p[1]
    if var in parser.variaveis: 
        p[0]=f"{parser.variaveis[var] and int(p[3])}"
        print(p[0])
    else:
        parser.error = (f"Variável {var} não definida")
        parser.exito = False

def p_ie_2Var(p):
    '''
    ie : ID IE ID
    '''
    var = p[1]
    var2 = p[3]
    if var in parser.variaveis: 
        if var2 in parser.variaveis:
            p[0]=f"{parser.variaveis[var] and parser.variaveis[var2]}"
            print(p[0])
        else:
            parser.error = (f"Variável {var2} não definida")
    else:
        parser.error = (f"Variável {var} não definida")
        parser.exito = False


def p_oue(p):
    '''
    oue : INT OUE INT
    '''
    p[0]=f"{int(p[1]) or int(p[3])}"
    print(p[0])

def p_oue_1Var(p):
    '''
    oue : INT OUE ID
    '''
    var = p[3]
    if var in parser.variaveis: 
        p[0]=f"{int(p[1]) or parser.variaveis[var]}"
        print(p[0])
    else:
        parser.error = (f"Variável {var} não definida")
        parser.exito = False

def p_oue_1Var1(p):
    '''
    oue : ID OUE INT
    '''
    var = p[1]
    if var in parser.variaveis: 
        p[0]=f"{parser.variaveis[var] or int(p[3])}"
        print(p[0])
    else:
        parser.error = (f"Variável {var} não definida")
        parser.exito = False

def p_oue_2Var(p):
    '''
    oue : ID OUE ID
    '''
    var = p[1]
    var2 = p[3]
    if var in parser.variaveis: 
        if var2 in parser.variaveis:
            p[0]=f"{parser.variaveis[var] or parser.variaveis[var2]}"
            print(p[0])
        else:
            parser.error = (f"Variável {var2} não definida")
    else:
        parser.error = (f"Variável {var} não definida")
        parser.exito = False

def p_noum(p):
    '''
    noum : NOUM ABREPC INT FECHAPC
    '''
    p[0]=f"{not int(p[3])}"

def p_noum_var(p):
    '''
    noum : NOUM ABREPC ID FECHAPC
    '''
    var = p[2]
    if var in parser.variaveis:
        p[0]= not parser.variaveis[var]
        print(p[0])
    else:
        parser.error = (f"Variável {var} não definida")
        parser.exito = False



def p_error(p):
    try:
        syntatic_sugar(p.value)
        parser.exito = False
    except:
        parser.error = (p)
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
