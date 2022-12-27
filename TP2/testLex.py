import ply.lex as lex

tokens = [
    "COMENTARIO",
    "VAR",
    "COM",
    "FLOAT",
    "INT",
    "ABREPC",
    "FECHAPC",
    "ID",
    "ALTERNA",
    'SOMA',
    'MENUS',
    'DIBIDE',
    'SOMANBEZES',
    'CHAPEU',
    'SOBRAS',
]

t_ABREPC = r'\('
t_FECHAPC = r'\)'
t_SOMA = r'\+'
t_MENUS = r'\-'
t_DIBIDE = r'\/'
t_SOMANBEZES = r'\*'
t_CHAPEU = r'\^'
t_SOBRAS = r'\%'

t_ignore = ' \r\n\t'

t_ID = "\w+"


def t_ALTERNA(t):
    r"alterna"
    t.type = "ALTERNA"
    return t


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


def t_error(t):
    print('Illegal character: ' + t.value[0])
    t.lexer.skip(1)
    return


lexer = lex.lex()
