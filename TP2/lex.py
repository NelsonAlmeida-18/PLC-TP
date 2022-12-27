import ply.lex as lex
import sys

tokens = [
    'COMENTARIO',
    'ABREPC',  # (
    'FECHAPC',  # )
    'ABREPR',  # [
    'FECHAPR',  # ]
    'FLOAT',
    'INT',
    'ID',
    'VAR',
    'COM',
    # condicional if
    "SERA",
    'LOGO',
    'SENAO',
    # ciclo while-do
    'ENQUANTO',
    'FAZ',
    # Operacoes Aritmeticas
    'SOMA',  # +
    'MENUS',  # -
    'DIBIDE',  # /
    'SOMANBEZES',  # *
    'CHAPEU',  # ^
    'SOBRAS',  # %
    # Operacoes Relacionais
    'MAISGRANDE',  # >
    'MAISPIQUENO',  # <
    'GEMEO',  # ==
    'MAISGRANDEOUGEMEO',  # >=
    'MAISPIQUENOOUGEMEO'  # <=
    # ler do stdin
    'ENTRADAS',
    # escrever no stdout
    'SAIDAS',
    # criar lista
    "LISTA",
    # indexacao
    "BUSCA",
    # criar matriz
    "MATRIZ"

]

t_ABREPC = r'\('
t_FECHAPC = r'\)'
t_ABREPR = r"\["
t_FECHAPR = r"\]"

t_SOMA = r'\+'
t_MENUS = r'\-'
t_DIBIDE = r'\/'
t_SOMANBEZES = r'\*'
t_CHAPEU = r'\^'
t_SOBRAS = r'\%'

t_ignore = ' \r\n\t'

t_ID = "\w+"


def t_FLOAT(t):
    r'\d+\.\d+'
    t.type = "FLOAT"
    return t


def t_INT(t):
    r'\d+'
    t.type = "INT"
    return t


def t_COMENTARIO(t):
    r'comentario'
    t.type = "COMENTARIO"
    return t


def t_VAR(t):
    r"var"
    t.type = "VAR"
    return t


def t_COM(t):
    r"com"
    t.type = "COM"
    return t


def t_SERA(t):
    r"sera"
    t.type = "SERA"
    return t


def t_LOGO(t):
    r"logo"
    t.type = "LOGO"
    return t


def t_SENAO(t):
    r"senao"
    t.type = "SENAO"
    return t


def t_ENQUANTO(t):
    r"enquanto"
    t.type = "ENQUANTO"
    return t


def t_FAZ(t):
    r"faz"
    t.type = "FAZ"
    return t


def t_PARA(t):
    r"para"
    t.type = "PARA"
    return t


def t_MAISGRANDE(t):
    r"maisgrande"
    t.type = "MAISGRANDE"
    return t


def t_MAISPIQUENO(t):
    r"maispiqueno"
    t.type = "MAISPIQUENO"
    return t


def t_MAISPIQUENOOUGEMEO(t):
    r"maispiquenoougemeo"
    t.type = "MAISPIQUENOOUGEMEO"
    return t


def t_MAISGRANDEOUGEMEO(t):
    r"maisgrandeougemeo"
    t.type = "MAISGRANDEOUGEMEO"
    return t


def t_ENTRADA(t):
    r"entrada"
    t.type = "ENTRADA"
    return t


def t_SAIDA(t):
    r"saida"
    t.type = "SAIDA"
    return t


def t_LISTA(t):
    r"lista"
    t.type = "LISTA"
    return t


def t_BUSCA(t):
    r"busca"
    t.type = "BUSCA"
    return t


def t_MATRIZ(t):
    r"matriz"
    t.type = "MATRIZ"
    return t


def t_error(t):
    print('Illegal character: ' + t.value[0])
    t.lexer.skip(1)
    return


# lexer = lex.lex()  # cria um AnaLex especifico a partir da especificação acima usando o gerador 'lex' do objeto 'lex'
# for linha in sys.stdin:
#    lexer.input(linha)
#    simb = lexer.token()
#    while simb:
#        print(simb)
#        simb = lexer.token()
