import ply.yacc as yacc
import sys

from lex import tokens


def p_COMENTARIO(p):
    "COMENTARIO : COMENTARIO ABREPC ID FECHAPC"


def p_VAR(p):
    '''VAR : VAR ID
           | VAR_COM
    '''
    parser.idVar += 1


def p_VAR_COM(p):
    "VAR : VAR id COM VALUE"
    parser.assignedVar += 1


def p_VALUE(p):
    '''
    VALUE : INT
          | FLOAT
          | ID
    '''


def p_error(p):
    print("Syntax error!")
    parser.exito = False


parser = yacc.yacc()

parser.exito = True
parser.idVar = 0
parser.assignedVar = 0

fonte = ""
for linha in sys.stdin:
    fonte += linha

parser.parse(fonte)

if parser.exito:
    print("Success")
    print(f"Numero de vars criadas(total): {parser.idVar}")
    print(f"Numero de vars criadas com valores: {parser.assignedVar}")
