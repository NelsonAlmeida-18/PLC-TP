import ply.yacc as yacc
import sys
import difflib
import random as rd

from testLex import tokens


def p_programa(p):
    '''
    programa : comentario
             | variavel
             | expr
    '''


def p_comentario(p):
    "comentario : COMENTARIO ABREPC ID FECHAPC"
    parser.numeroComents += 1
    parser.linhaDeCodigo += 1


def p_variavel(p):
    "variavel : Decl"
    p[0] = p[1]


def p_Decl_NoAssign(p):
    "Decl : VAR ID"
    varName = p[2]
    parser.linhaDeCodigo += 1
    if varName not in parser.variaveis:
        parser.variaveis[varName] = None
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} já definida.")
        parser.exito = False


def p_Decl_FLOAT(p):
    "Decl : VAR ID COM FLOAT"
    parser.vars += 1
    varName = p[2]
    varValue = p[4]
    parser.linhaDeCodigo += 1
    if varName not in parser.variaveis:
        parser.variaveis[varName] = float(varValue)
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} já definida.")
        parser.exito = False


def p_Decl_INT(p):
    "Decl : VAR ID COM INT"
    parser.vars += 1
    varName = p[2]
    varValue = p[4]
    parser.linhaDeCodigo += 1
    if varName not in parser.variaveis:
        parser.variaveis[varName] = int(varValue)
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} já definida.")
        parser.exito = False


def p_Decl_SOMA(p):
    "Decl : VAR ID COM soma"
    parser.vars += 1
    varName = p[2]
    varValue = p[4]
    parser.linhaDeCodigo += 1
    if varName not in parser.variaveis:
        parser.variaveis[varName] = varValue
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} já definida.")
        parser.exito = False


def p_Decl_String(p):
    "Decl : VAR ID COM ID"
    parser.vars += 1
    varName = p[2]
    varValue = p[4]
    parser.linhaDeCodigo += 1
    if varName not in parser.variaveis:
        parser.variaveis[varName] = varValue
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} já definida.")
        parser.exito = False


def p_Expressao(p):
    '''expr : alteraVar
            | soma
            | sub
    '''
    p[0] = p[1]


def p_alteraVar_String(p):
    "alteraVar : ALTERNA ID COM ID"
    varName = p[2]
    varValue = p[4]
    parser.linhaDeCodigo += 1
    if varName in parser.variaveis:
        parser.variaveis[varName] = varValue
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} não definida anteriormente.")
        parser.exito = False


def p_alteraVar_soma(p):
    "alteraVar : ALTERNA ID COM soma"
    varName = p[2]
    varValue = p[4]
    parser.linhaDeCodigo += 1
    if varName in parser.variaveis:
        parser.variaveis[varName] = varValue
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} não definida anteriormente.")
        parser.exito = False


def p_alteraVar_Float(p):
    "alteraVar : ALTERNA ID COM FLOAT"
    varName = p[2]
    varValue = p[4]
    parser.linhaDeCodigo += 1
    if varName in parser.variaveis:
        parser.variaveis[varName] = float(varValue)
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} não definida anteriormente.")
        parser.exito = False


def p_alteraVar_Int(p):
    "alteraVar : ALTERNA ID COM INT"
    varName = p[2]
    varValue = p[4]
    parser.linhaDeCodigo += 1
    if varName in parser.variaveis:
        parser.variaveis[varName] = int(varValue)
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} não definida anteriormente.")
        parser.exito = False


def p_soma_int(p):
    '''
    soma : INT SOMA INT
    '''
    # assembly faz a operaçao???
    p[0] = int(p[1]) + int(p[3])


def p_soma_var_int(p):
    '''
    soma : ID SOMA INT
    '''
    varName = p[1]
    if varName in parser.variaveis:
        parser.variaveis[varName] += int(p[3])
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} não definida anteriormente.")


def p_soma_var_float(p):
    '''
    soma : ID SOMA FLOAT
    '''
    varName = p[1]
    if varName in parser.variaveis:
        parser.variaveis[varName] += float(p[3])
    else:
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} não definida anteriormente.")


# não deveria verificar se são duas strings? para concatenação de strings?
def p_soma_var_var(p):
    '''
    soma : ID SOMA ID
    '''
    varName = p[1]
    varName2 = p[3]
    if varName in parser.variaveis and varName2 in parser.variaveis:
        parser.variaveis[varName] += parser.variaveis[varName2]
    elif varName in parser.variaveis:
        parser.variaveis[varName] += p[3]
    elif varName2 in parser.variaveis:
        parser.variaveis[varName2] = p[3]+parser.variaveis[varName2]
    else:
        # deveria ser soma de strings mas não faz sentido não ser atribuido a nada
        print(
            f"Erro na linha {parser.linhaDeCodigo}: Variável {varName} não definida anteriormente.")


def p_soma_float(p):
    '''
    soma : FLOAT SOMA FLOAT
         | FLOAT SOMA INT
         | INT SOMA FLOAT
    '''
    # assembly faz a operaçao???
    p[0] = float(p[1]) + float(p[3])


def p_menus_int_int(p):
    '''
    sub : INT MENUS INT
    '''
    p[0] = int(p[1]) - int(p[3])


def p_menus_float_float(p):
    '''
    sub : FLOAT MENUS FLOAT
         | FLOAT MENUS INT
         | INT MENUS FLOAT
    '''
    # assembly faz a operaçao???
    p[0] = float(p[1]) - float(p[3])


def p_error(p):
    syntatic_sugar(p.value)
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

for line in sys.stdin:
    parser.exito = True
    parser.parse(line)
    if parser.exito:
        print("--------------------------------------")
        print(f"Numero de vars criadas(total): {parser.vars}")
        print(f"Numero de comentarios: {parser.numeroComents}")
        print(f"Variáveis: {parser.variaveis}")
        print("--------------------------------------")
    else:
        print("--------------------------------------")
        print("Erro ao compilar.")
        print(parser.error)
        print("--------------------------------------")
        break
