import ply.lex as lex
import sys


class lexer:
    def __init__(self):
        self.lexer()

    def lexer(self):
        tokens = [
            'COMENTARIO',
            'LPAREN',
            'RPAREN',
            'VAR',
            'COM',
            # condicional if
            "SERA",
            'LOGO',
            'SENAO',
            # ciclo while-do
            'ENQUANTO',
            'FAZ',
            # operacoesAritmeticas
            'SOMA',
            'PERDESTE',
            'DIBIDE',
            'SOMANBEZES',
            'PAU',
            'SOBRAS',
            # operacoes relacionais
            'MAISGRANDE',
            'MAISPIQUENO',
            'GEMEO',
            'MAISGRANDEOUGEMEO',
            'MAISPIQUENOOUGEMEO'
            # ler do stdin
            'ENTRADAS',
            # escrever no stdout
            'SAIDAS',
            # criar lista
            "LISTA",
            # indexacao
            "BUSCA",
            # criar matriz
            "MATRIZ",


        ]

        t_LPAREN = r'\('
        t_RPAREN = r'\)'

        t_ignore = ' \r\n\t'

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

        def t_error(t):
            print('Illegal character: ' + t.value[0])
            t.lexer.skip(1)
            return

        lexer = lex.lex()  # cria um AnaLex especifico a partir da especificação acima usando o gerador 'lex' do objeto 'lex'
        for linha in sys.stdin:
            lexer.input(linha)
            simb = lexer.token()
            while simb:
                print(simb)
                simb = lexer.token()


lexer()
