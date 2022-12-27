import ply.yacc as yacc
import sys

from testLex import tokens


def p_exprArit(p):
    '''
    exprArit : soma
             | sub
             | mult
             | div
             | exp
             | mod
    '''


# SOMA COM RESULTADO INT
def p_soma_int_int(p):
    '''
    soma : INT SOMA INT
    '''
    # assembly faz a operaçao???
    p[0] = int(p[1]) + int(p[3])


# SOMA COM RESULTADO FLOAT
def p_soma_float(p):
    '''
    soma : FLOAT SOMA FLOAT
         | FLOAT SOMA INT
         | INT SOMA FLOAT
    '''
    # assembly faz a operaçao???
    p[0] = float(p[1]) + float(p[3])


# SUBTRAI COM RESULTADO INT
def p_menus_int_int(p):
    '''
    sub : INT MENUS INT
    '''
    p[0] = int(p[1]) - int(p[3])


# SUBTRAI COM RESULTADO FLOAT
def p_menus_float_float(p):
    '''
    sub : FLOAT MENUS FLOAT
        | FLOAT MENUS INT
        | INT MENUS FLOAT
    '''
    # assembly faz a operaçao???
    p[0] = float(p[1]) - float(p[3])


# MULTIPLICA COM RESULTADO INT
def p_somanbezes_int(p):
    '''
    mult : INT SOMANBEZES INT
    '''
    # assembly faz a operaçao???
    p[0] = int(p[1]) * int(p[3])


# MULTIPLICA COM RESULTADO FLOAT
def p_somanbezes_float(p):
    '''
    mult : FLOAT SOMANBEZES FLOAT
         | FLOAT SOMANBEZES INT
         | INT SOMANBEZES FLOAT
    '''
    # assembly faz a operaçao???
    p[0] = float(p[1]) + float(p[3])


# DIVIDE COM RESULTADO INT
def p_div_int_int(p):
    '''
    div : INT DIBIDE INT
    '''
    # assembly faz a operaçao???
    p[0] = int(p[1]) / int(p[3])


# DIVIDE COM RESULTADO FLOAT
def p_div_float(p):
    '''
    div  : FLOAT DIBIDE FLOAT
         | FLOAT DIBIDE INT
         | INT DIBIDE FLOAT
    '''
    # assembly faz a operaçao???
    p[0] = float(p[1]) / float(p[3])


# EXPONE COM RESULTADO INT
def p_exp_int_int(p):
    '''
    exp : INT CHAPEU INT
    '''
    # assembly faz a operaçao???
    p[0] = int(p[1]) ^ int(p[3])


# SOMA COM RESULTADO FLOAT
def p_exp_float(p):
    '''
    exp : FLOAT CHAPEU FLOAT
        | FLOAT CHAPEU INT
        | INT CHAPEU FLOAT
    '''
    # assembly faz a operaçao???
    p[0] = float(p[1]) ^ float(p[3])


# RESTO DA DIVISÃO COM RESULTADO INT
def p_mod_int_int(p):
    '''
    mod : INT SOBRAS INT
    '''
    # assembly faz a operaçao???
    p[0] = int(p[1]) % int(p[3])


# RESTO DA DIVISÃO COM RESULTADO FLOAT
def p_mod_float(p):
    '''
    mod : FLOAT SOBRAS FLOAT
        | FLOAT SOBRAS INT
        | INT SOBRAS FLOAT
    '''
    # assembly faz a operaçao???
    p[0] = float(p[1]) % float(p[3])
