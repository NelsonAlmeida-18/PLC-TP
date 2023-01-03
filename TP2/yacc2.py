import ply.yacc as yacc
import sys

import difflib
import random as rd
import math

from lex2 import tokens


def p_programa(p):
    '''
    programa : corpo
    '''
    print("teste")
    parser.assembly = f"START\n{p[1]}STOP"

def p_programa_decls(p):
    '''
    programa : decl
    '''
    parser.assembly = f"{p[1]}"

# falta adicionar ciclos

def p_programa_rec(p):
    '''
    programa : decl corpo
    '''
    parser.assembly = f"{p[1]}START\n{p[2]}STOP"



def p_entrada_ID(p):
    '''
    entrada : ID
    '''
    varName = p[1]
    if varName not in parser.variaveis:
        parser.error = f"Variável {varName} não declarada anteriormente"
        parser.sucesso = False
    else:
        p[0] = parser.variaveis[varName]


def p_entrada_INT(p):
    '''
    entrada : INT
    '''
    p[0] = int(p[1])


# Comentário
def p_decl_comentario(p):
    "decl : COMENTARIO ABREPC STRING FECHAPC"


# Criar varável sem valor
def p_decl_NoAssign(p):
    '''
    decl : VAR ID
    '''
    varName = p[2]
    print(varName)
    if varName not in parser.variaveis:
        parser.variaveis[varName] = (None, parser.stackPointer)
        parser.vars += 1
        p[0] = f"PUSHI 0\n"
        parser.stackPointer += 1
        # TO REview push 0?
    else:
        parser.error = (f"Variável {varName} já definida.")
        parser.exito = False


# Criar variável com valor INT
def p_decl_Int(p):
    '''
    decl : VAR ID COM entrada
    '''
    varName = p[2]
    value = p[4]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = (value, parser.stackPointer)
        p[0] = f"PUSHI {value}\n"
        parser.vars += 1
        parser.stackPointer += 1
    else:
        parser.error = (f"Variável {varName[1]} já definida.")
        parser.exito = False


# Criar variável com valor de uma expressão
def p_decl_op(p):
    '''
    decl : VAR ID COM op
    '''
    varName = p[2]
    varValue = p[4]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = (varValue, parser.stackPointer)
        parser.vars += 1
        p[0] = f"PUSHI {varValue}\n"
        parser.stackPointer += 1
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
        parser.variaveis[listName] = ([], parser.stackPointer)
        parser.vars += 1
        p[0] = f"PUSHN 0\n"
        parser.stackPointer += 1
    else:
        parser.error = (
            f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Cria Array com tamanho
def p_decl_Lista(p):
    '''
    decl : LISTA ID entrada
    '''
    listName = p[2]
    size = p[3]
    if listName not in parser.variaveis:
        parser.variaveis[listName] = (
            [None for i in range(size)], parser.stackPointer
        )
        parser.vars += 1
        p[0] = f"PUSHN {size}\n"
        parser.stackPointer += size
    else:
        parser.error = (
            f"Variável com o nome {listName} já definida anteriormente."
        )
        parser.exito = False


# Cria Matriz sem tamanho
def p_decl_Matriz_NoSize(p):
    '''
    decl : MATRIZ ID
    '''
    matrizName = p[2]
    if matrizName not in parser.variaveis:
        parser.variaveis[matrizName] = ([[]], parser.stackPointer)
        parser.vars += 1
        p[0] = f"PUSHN 0\n"
        parser.stackPointer += 1
    else:
        parser.error = (f"Matriz {matrizName} já definida.")
        parser.exito = False


# Cria Matriz com tamanho
def p_decl_Matriz(p):
    '''
    decl : MATRIZ ID entrada entrada
    '''
    matrizName = p[2]
    size1 = p[3]
    size2 = p[4]
    if matrizName not in parser.variaveis:
        parser.variaveis[matrizName] = (
            [[None for j in range(size1)] for i in range(size2)], parser.stackPointer)
        parser.vars += 1
        p[0] = f"PUSHN {size1 * size2}\n"
        parser.stackPointer += size1*size2
    else:
        parser.error = (f"Matriz {matrizName} já definida.")
        parser.exito = False


# Altera o valor de uma variável para um INT
def p_alternaVar(p):
    '''
    alterna : ALTERNA ID COM entrada
    '''
    varName = p[2]
    value = p[4]
    if varName in parser.variaveis:
        parser.variaveis[varName] = (value, parser.variaveis[varName])
    else:
        parser.error = (f"Variável {varName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma variável para o resultado de uma expressao
def p_alternaVar_op(p):
    '''
    alterna : ALTERNA ID COM op
    '''
    varName = p[2]
    value = p[4]
    if varName in parser.variaveis:
        parser.variaveis[varName] = (value, parser.variaveis[varName])
    else:
        parser.error = (f"Variável {varName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma lista numa dada posicao pelo de um inteiro
def p_alternaLista(p):
    '''
    alterna : ALTERNA ID entrada COM entrada
    '''
    arrayName = p[2]
    indexForReplacement = p[3]
    valueForReplacement = p[5]
    if arrayName in parser.variaveis:
        if indexForReplacement < len(parser.variaveis[arrayName]):
            parser.variaveis[arrayName][indexForReplacement][0] = valueForReplacement
        else:
            parser.error = (f"Indice fora de alcance")
            parser.exito = False
    else:
        parser.error = (f"Variável {arrayName} não definida anteriormente.")
        parser.exito = False


# Altera o valor de uma lista numa dada posicao pelo de uma expressao aritmetica
def p_alternaLista_op(p):
    '''
    alterna : ALTERNA ID entrada COM op
    '''
    arrayName = p[2]
    indexForReplacement = p[3]
    valueForReplacement = p[5]
    if arrayName in parser.variaveis:
        if indexForReplacement < len(parser.variaveis[arrayName]):
            parser.variaveis[arrayName][indexForReplacement] = (valueForReplacement, parser.variaveis[arrayName][1])
        else:
            parser.error = (f"Indice fora de alcance")
            parser.exito = False
    else:
        parser.error = (f"Variável {arrayName} não definida anteriormente.")
        parser.exito = False


def p_corpo(p):
    '''
    corpo   : proc
    '''
    p[0]=p[1]

def p_corpo_rec(p):
    '''
    corpo : corpo proc
    '''
    p[0] = f"{p[1]}{p[2]}"

def p_proc_alterna(p):
    '''
    proc : alterna
    '''
    p[0] = p[1]

#adicionar expressoes entrada, if then else..


def p_op(p):
    '''
    op : ExprArit
       | ExprRel
       | ExprLog
       | Busca
    '''
    p[0] = p[1]


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
    soma : entrada SOMA entrada
    '''
    val1 = p[1]
    val2 = p[3]
    if val1 != None and val2 != None or isinstance(val1, type(val2)):
        p[0] = f"{val1}{val2}ADD\n"
    else:
        parser.error = (
            f"Operação impossível entre os tipo de dados {type(val1)}, {type(val2)}!")
        parser.exito = False


# Subtração
def p_sub(p):
    '''
    sub : entrada MENUS entrada
    '''
    val1 = p[1]
    val2 = p[3]
    if isinstance(val1, type(val2)) and isinstance(val1, int):
        p[0] = f"{val1}{val2}SUB\n"
    else:
        parser.error = (
            f"Operação impossível entre os tipo de dados {type(val1)}, {type(val2)}!")
        parser.exito = False


# Multiplicação
def p_mult(p):
    '''
    mult : entrada SOMANBEZES entrada
    '''
    val1 = p[1]
    val2 = p[3]
    if isinstance(val1, list) and isinstance(val2, int) or isinstance(val1, int) and isinstance(val2, list):
        p[0] = f"{val1}{val2}MUL\n"
    else:
        parser.error = (
            f"Operação impossível entre os tipo de dados {type(val1)}, {type(val2)}!")
        parser.exito = False


# Divisão
def p_div(p):
    '''
    div : entrada DIBIDE entrada
    '''
    val1 = p[1]
    val2 = p[3]
    if isinstance(val1, type(val2)) and isinstance(val1, int):
        p[0] = f"{val1}{val2}DIV\n"
    else:
        parser.error = (
            f"Operação impossível entre os tipo de dados {type(val1)}, {type(val2)}!")
        parser.exito = False


# Exponenciação
def p_exp(p):
    '''
    exp : entrada CHAPEU entrada
    '''
    val1 = p[1]
    val2 = p[3]
    if isinstance(val1, type(val2)) and isinstance(val1, int):
        entrada = ""
        for i in range(val2):
            entrada+=f"PUSHI {val1}\n"
        for i in range(val2-1):
            entrada+=f"MUL\n"
        p[0] = entrada
    else:
        parser.error = (
            f"Operação impossível entre os tipo de dados {type(val1)}, {type(val2)}!")
        parser.exito = False


# Resto da divisão
def p_resto(p):
    '''
    resto : entrada SOBRAS entrada
    '''
    val1 = p[1]
    val2 = p[3]
    if isinstance(val1, type(val2)) and isinstance(val1, int):
        p[0] = f"{val1}{val2}MOD\n"
    else:
        parser.error = (
            f"Operação impossível entre os tipo de dados {type(val1)}, {type(val2)}!")
        parser.exito = False


# Retorna o elemento no indice do array
def p_Busca_Lista(p):
    '''
    Busca : BUSCA ID entrada
    '''
    matrizName = p[2]
    indice1 = p[3]
    if isinstance(parser.variaveis[matrizName], int) or parser.variaveis[matrizName] == None:
        parser.error = ("Operação inválida sobre o tipo de dados")
        parser.exito = False
    elif isinstance(indice1, int) and indice1 < len(parser.variaveis[matrizName]):
        p[0] = f"{parser.variaveis[matrizName][indice1][0]}"
    else:
        parser.error = (f"Indice fora de alcance")
        parser.exito = False


# Retorna o elemento no indice da matriz
def p_Busca_Matriz(p):
    '''
    Busca : BUSCA ID entrada entrada
    '''
    matrizName = p[2]
    indice1 = p[3]
    indice2 = p[4]
    if isinstance(parser.variaveis[matrizName], int) or parser.variaveis[matrizName] == None:
        parser.error = ("Operação inválida sobre o tipo de dados")
        parser.exito = False
    elif isinstance(indice1, int) and isinstance(indice2, int) and indice1 < len(parser.variaveis[matrizName]) and indice2 < len(parser.variaveis[matrizName][indice1]):
        p[0] = parser.variaveis[matrizName][indice1][indice2]
    else:
        parser.error = (f"Indice fora de alcance")
        parser.exito = False


# Operações Relativas
def p_ExprRel(p):
    '''
    ExprRel : maisGrande
            | maisPiqueno
            | gemeo
            | maisGrandeOuGemeo
            | maisPiquenoOuGemeo
            | naoGemeo
    '''
    p[0] = p[1]


# Operação Maior (>)
def p_maisGrande(p):
    '''
    maisGrande : MAISGRANDE ABREPC entrada VIRG entrada FECHAPC
    '''
    val1 = p[3]
    val2 = p[5]
    if isinstance(val1, type(val2)):
        p[0] = f"{p[3]}{p[5]}SUP\n"
    else:
        parser.error = f"Operação inválida entre o tipo de dados {type(val1)}, {type(val2)}"
        parser.exito = False


# Operação Menor (<)
def p_maisPiqueno(p):
    '''
    maisPiqueno : MAISPIQUENO ABREPC entrada VIRG entrada FECHAPC
    '''
    val1 = p[3]
    val2 = p[5]
    if isinstance(val1, type(val2)):
        p[0] = f"{p[3]}{p[5]}INF\n"
    else:
        parser.error = f"Operação inválida entre o tipo de dados {type(val1)}, {type(val2)}"
        parser.exito = False


# Operação Egual (==)
def p_gemeo(p):
    '''
    gemeo : GEMEO ABREPC entrada VIRG entrada FECHAPC
    '''
    val1 = p[3]
    val2 = p[5]
    if isinstance(val1, type(val2)):
        p[0] = f"{p[3]}{p[5]}EQUAL\n"
    else:
        parser.error = f"Operação inválida entre o tipo de dados {type(val1)}, {type(val2)}"
        parser.exito = False


# Operação Maior ou Igual (>=)
def p_maisGrandeOuGemeo(p):
    '''
    maisGrandeOuGemeo : MAISGRANDEOUGEMEO ABREPC entrada VIRG entrada FECHAPC
    '''
    val1 = p[3]
    val2 = p[5]
    if isinstance(val1, type(val2)):
        p[0] = f"{p[3]}{p[5]}SUPEQ\n"
    else:
        parser.error = f"Operação inválida entre o tipo de dados {type(val1)}, {type(val2)}"
        parser.exito = False


# Operação Menor ou Igual (<=)
def p_maisPiquenoOuGemeo(p):
    '''
    maisPiquenoOuGemeo : MAISPIQUENOOUGEMEO ABREPC entrada VIRG entrada FECHAPC
    '''
    val1 = p[3]
    val2 = p[5]
    if isinstance(val1, type(val2)):
        p[0] = f"{p[3]}{p[5]}INFEQ\n"
    else:
        parser.error = f"Operação inválida entre o tipo de dados {type(val1)}, {type(val2)}"
        parser.exito = False


# Operação Diferente (!=)
def p_naoGemeo(p):
    '''
    naoGemeo : NAOGEMEO ABREPC entrada VIRG entrada FECHAPC
    '''
    val1 = p[3]
    val2 = p[5]
    if isinstance(val1, type(val2)):
        p[0] = f"{p[3]}{p[5]}NOT\nEQUAL\n"
    else:
        parser.error = f"Operação inválida entre o tipo de dados {type(val1)}, {type(val2)}"
        parser.exito = False


# Operações Logicas
def p_ExprLog(p):
    '''
    ExprLog : ie
            | oue
            | noum
    '''
    p[0] = p[1]


# Operação E
def p_ie(p):
    '''
    ie : entrada IE entrada
    '''
    val1 = p[1]
    val2 = p[3]
    if isinstance(val1, type(val2)):
        p[0] = f"{p[3] and p[5]}"
    else:
        parser.error = f"Operação inválida entre o tipo de dados {type(val1)}, {type(val2)}"
        parser.exito = False


# Operação Ou
def p_oue(p):
    '''
    oue : entrada OUE entrada
    '''
    val1 = p[1]
    val2 = p[3]
    if isinstance(val1, type(val2)):
        p[0] = f"{p[3]}{p[5]}NOT\n"
    else:
        parser.error = f"Operação inválida entre o tipo de dados {type(val1)}, {type(val2)}"
        parser.exito = False


# Operação Não
def p_noum(p):
    '''
    noum : NOUM ABREPC entrada FECHAPC
    '''
    val1 = p[3]
    if isinstance(val1, int):
        p[0] = f"{p[3]}NOT"
    else:
        parser.error = f"Operação inválida com o tipo de dados {type(val1)}"
        parser.exito = False


def p_error(p):
    try:
        syntatic_sugar(p.value)
        parser.exito = False
    except:
        parser.error = (p)
        parser.exito = False


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
parser.assembly = ""
parser.stackPointer = 0
parser.exito = True

for line in sys.stdin:
    parser.exito = True
    parser.parse(line)
    if parser.exito:
        print("--------------------------------------")
        print(f"Variáveis: {parser.variaveis}")
        print(parser.assembly)
        print("--------------------------------------")
    else:
        print("--------------------------------------")
        print(parser.error)
        print("--------------------------------------")
        break
