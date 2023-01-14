import ply.lex as lex

tokens = [
    "STRING",
    "ID",
    "VAR",
    "COM",

    "ABREPC",
    "FECHAPC",
    "ABREPR",
    "FECHAPR",
    "ABRECHAV",
    "FECHACHAV",
    "VIRG",

    "INT",

    'SOMA',
    'MENUS',
    'SOMANBEZES',
    'DIBIDE',
    'SOBRAS',

    'MAISGRANDE',
    'MAISPIQUENO',
    'GEMEO',
    'NAOGEMEO',
    'MAISGRANDEOUGEMEO',
    'MAISPIQUENOOUGEMEO',

    'IE',
    'OUE',
    'NOUM',

    "ALTERNA",

    "LISTA",
    "MATRIZ",
    "BUSCA",
    "SWAP",

    "SENAO",
    "SE",
    "ENTAO",
    "FIM",

    "ENQUANTO",
    "FAZ",

    "ENTRADAS",
    "SAIDAS"
]

t_ignore = ' \r\n\t'

t_ABRECHAV = r"\{"
t_FECHACHAV = r"\}"
t_ABREPC = r'\('
t_FECHAPC = r'\)'
t_ABREPR = r'\['
t_FECHAPR = r'\]'
t_VIRG = r'\,'
t_SOMA = r'\+'
t_MENUS = r'\-'
t_SOMANBEZES = r'\*'
t_DIBIDE = r'\/'
t_SOBRAS = r'\%'
t_STRING = r"\"[w+d+]*\"|\'[w+d+]*\'"

t_ID = r"\w+"


def t_INT(t):
    r'\d+'
    t.type = "INT"
    return t


def t_COMENTARIO(t):
    r'comentario'
    t.type = "COMENTARIO"
    return t


def t_VAR(t):
    r'var'
    t.type = "VAR"
    return t


def t_COM(t):
    r'com'
    t.type = "COM"
    return t


def t_ALTERNA(t):
    r'alterna'
    t.type = "ALTERNA"
    return t


def t_MAISGRANDE(t):
    r"maisGrande"
    t.type = "MAISGRANDE"
    return t


def t_MAISPIQUENO(t):
    r"maisPiqueno"
    t.type = "MAISPIQUENO"
    return t


def t_NAOGEMEO(t):
    r"naogemeo"
    t.type = "NAOGEMEO"
    return t


def t_GEMEO(t):
    r"gemeo"
    t.type = "GEMEO"
    return t


def t_MAISGRANDEOUGEMEO(t):
    r"maisGrandeOuGemeo"
    t.type = "MAISGRANDEOUGEMEO"
    return t


def t_MAISPIQUENOOUGEMEO(t):
    r"maisPiquenoOuGemeo"
    t.type = "MAISPIQUENOOUGEMEO"
    return t


def t_IE(t):
    r"ie"
    t.type = "IE"
    return t


def t_OUE(t):
    r"oue"
    t.type = "OUE"
    return t


def t_NOUM(t):
    r"noum"
    t.type = "NOUM"
    return t


def t_LISTA(t):
    r'lista'
    t.type = "LISTA"
    return t


def t_MATRIZ(t):
    r'matriz'
    t.type = "MATRIZ"
    return t


def t_BUSCA(t):
    r'busca'
    t.type = "BUSCA"
    return t


def t_SWAP(t):
    r'swap'
    t.type = "SWAP"
    return t


def t_SENAO(t):
    r'senao'
    t.type = "SENAO"
    return t


def t_SE(t):
    r'se'
    t.type = "SE"
    return t


def t_ENTAO(t):
    r'entao'
    t.type = "ENTAO"
    return t


def t_ENQUANTO(t):
    r'enquanto'
    t.type = "ENQUANTO"
    return t


def t_FAZ(t):
    r'faz'
    t.type = "FAZ"
    return t


def t_FIM(t):
    r'fim'
    t.type = "FIM"
    return t


def t_ENTRADAS(t):
    r"entradas"
    t.type = "ENTRADAS"
    return t


def t_SAIDAS(t):
    r"saidas"
    t.type = "SAIDAS"
    return t


def t_error(t):
    print('Illegal character: ' + t.value[0])
    t.lexer.skip(1)
    return


lexer = lex.lex()
