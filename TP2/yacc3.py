import ply.yacc as yacc
import random as rd

from lex2 import *
import sys


def p_Programa_Empty(p):
    '''
    Programa : Decls
             | Atrib
    '''
    parser.assembly = f'{p[1]}'


def p_Programa(p):
    '''
    Programa : Decls Corpo
    '''
    parser.assembly = f'{p[1]}START\n{p[2]}STOP\n'


def p_Programa_Corpo(p):
    '''
    Programa : Corpo
    '''
    parser.assembly = f"START\n{p[1]}STOP\n"


def p_Corpo(p):
    '''
    Corpo : Proc
          | Atrib
    '''
    p[0] = f"{p[1]}"


def p_Corpo_Rec(p):
    '''
    Corpo : Proc Corpo
          | Atrib Corpo
    '''
    p[0] = f"{p[1]}{p[2]}"


def p_Decls(p):
    "Decls : Decl"
    p[0] = f'{p[1]}'


def p_DeclsRec(p):
    "Decls : Decls Decl"
    p[0] = f'{p[1]}{p[2]}'


def p_expr_arit(p):
    '''
    expr : exprArit
         | exprRel
    '''
    p[0] = p[1]


def p_Proc(p):
    '''
    Proc : if
         | while
         | saidas
    '''
    p[0] = p[1]


# Declaração de uma variavel sem valor
def p_Decl(p):
    "Decl : VAR ID"
    varName = p[2]
    if varName not in parser.variaveis:
        parser.variaveis[varName] = (None, parser.stackPointer)
        p[0] = "PUSHI 0\n"
        parser.stackPointer += 1
    else:
        parser.exito = False
        parser.error = f"Variável com o nome {varName} já existe"


# Declaração de uma variável com atribuição de um valor
def p_Atrib_expr(p):
    "Atrib : VAR ID COM expr"
    varName = p[2]
    if varName not in parser.variaveis:
        value = p[4]
        parser.variaveis[varName] = (value, parser.stackPointer)
        p[0] = f"{value}STOREG {parser.stackPointer}\n"
        parser.stackPointer += 1
    else:
        parser.exito = False
        parser.error = f"Variável com o nome {varName} já existe"


# Altera valor de um variável
def p_alterna_var(p):
    '''Atrib : ALTERNA ID COM expr'''
    varName = p[2]
    if varName in parser.variaveis:
        parser.variaveis[varName] = (p[4], parser.variaveis[varName][1])
        p[0] = f"{p[4]}STOREG {parser.variaveis[varName][1]}\n"


def p_expr(p):
    "expr : INT"
    p[0] = f"PUSHI {int(p[1])}\n"


def p_expr_var(p):
    "expr : ID"
    varName = p[1]
    if varName in parser.variaveis:
        p[0] = f"PUSHG {parser.variaveis[varName][1]}\n"


def p_expr_entradas(p):
    "expr : ENTRADAS"
    p[0] = f"READ\nATOI\n"


# Declara lista sem tamanho
def p_Decl_Lista_NoSize(p):
    "Decl : LISTA ID"
    listName = p[2]
    if listName not in parser.variaveis:
        parser.variaveis[listName] = (parser.stackPointer, 0)
        p[0] = f"PUSHN 0\n"
        parser.stackPointer += 1
    else:
        parser.error = (
            f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Declara lista com tamanho INT
def p_DeclLista_Size(p):
    "Decl : LISTA ID INT"
    listName = p[2]
    size = int(p[3])
    if listName not in parser.variaveis:
        if size > 0:
            parser.variaveis[listName] = (parser.stackPointer, size)
            p[0] = f"PUSHN {size}\n"
            parser.stackPointer += size
        else:
            parser.error = f"Impossível declarar um array de tamanho {size}"
            parser.exito = False
    else:
        parser.error = (
            f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Atribui valores à lista com outra lista
def p_AtribLista_lista(p):
    "Atrib : LISTA ID COM lista"
    lista = p[4]
    varName = p[2]
    if varName in parser.variaveis:
        if len(lista)<parser.variaveis[varName][1]:
            assm = ""
            for i in lista:
                assm += f"PUSHI {i}\n"

            parser.variaveis[varName] = (parser.stackPointer, parser.variaveis[varName][1])
            parser.stackPointer += len(lista)
            p[0] = assm
        else:
            parser.error = f"Variável com o nome {varName} não definida"
            parser.exito = False
    else:
        assm = ""
        for i in lista:
            assm += f"PUSHI {i}\n"

        parser.variaveis[varName] = (parser.stackPointer, len(lista))
        parser.stackPointer += len(lista)
        p[0] = assm



# Altera valor de um indice da lista
def p_AlternaLista_elem(p):
    "Atrib : ALTERNA ID ABREPR expr FECHAPR COM expr"
    varName = p[2]
    pos = p[4]
    if varName in parser.variaveis:
        if pos < parser.variaveis[varName][1]:
            p[0] = f"PUSHGP\nPUSHI {parser.variaveis[varName][1]}\nPADD\n{p[4]}{p[7]}STOREN\n"
        else:
            parser.error = f"Indice {pos} fora de alcance"
            parser.exito = False
    else:
        parser.error = f"Variável com o nome {varName} não definida"
        parser.exito = False


# Declara lista sem tamanho
def p_Decl_Matriz_NoSize(p):
    "Decl : MATRIZ ID"
    listName = p[2]
    if listName not in parser.variaveis:
        parser.variaveis[listName] = (parser.stackPointer, 0, 0)
        p[0] = f"PUSHN 0\n"
        parser.stackPointer += 1
    else:
        parser.error = (
            f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Declara matriz com tamanho INT INT
def p_DeclMatriz_Size(p):
    "Decl : MATRIZ ID INT INT"
    listName = p[2]
    size = int(p[3])
    size1 = int(p[4])
    if listName not in parser.variaveis:
        parser.variaveis[listName] = (parser.stackPointer, size, size1)
        p[0] = f"PUSHN {size*size1}\n"
        parser.stackPointer += size*size1
    else:
        parser.error = (
            f"Variável com o nome {listName} já definida anteriormente.")
        parser.exito = False


# Função que altera o valor de um indice da matriz por outro
def p_AtribMatriz_comExpr(p):
    "Atrib : ALTERNA ID ABREPR expr FECHAPR ABREPR expr FECHAPR COM expr"
    matName = p[2]
    if matName in parser.variaveis:
        if len(parser.variaveis[matName]):
            p[0] = f'''PUSHGP\nPUSHI {parser.variaveis[matName][0]}\nPADD\n{p[4]}PUSHI {parser.variaveis[matName][2]}MUL\nPADD\n{p[7]}{p[10]}STOREN\n'''
        else:
            parser.error = f"Operação inválida, variável {matName} não é uma matriz"
            parser.exito = False
    else:
        parser.error = f"Variável não declarada anteriormente"
        parser.exito = False


# Função que altera uma lista da matriz por outra
def p_AtribMatriz_comLista(p):
    "Atrib : ALTERNA ID ABREPR expr FECHAPR COM lista"
    matName = p[2]
    if matName in parser.variaveis:
        if len(parser.variaveis[matName]) == 3:
            if len(p[7]) <= parser.variaveis[matName][2]:
                assm = ""
                j = 0
                for i in p[7]:
                    assm += f'''PUSHGP\nPUSHI {parser.variaveis[matName][0]}\nPADD\n{p[4]}PUSHI {parser.variaveis[matName][2]}\nMUL\nPADD\nPUSHI {j}\nPUSHI {i}\nSTOREN\n'''
                    j += 1
                p[0] = f'{assm}'
            else:
                parser.error = f"Tamanho da lista maior do que o alocado"
                parser.exito = False
        else:
            parser.error = f"Operação inválida, variável {matName} não é uma matriz"
            parser.exito = False
    else:
        parser.error = f"Variável não declarada anteriormente"
        parser.exito = False


# Função que vai buscar o valor do indice na lista
def p_ProcBusca_Lista(p):
    "Proc : BUSCA ID ABREPR expr FECHAPR"
    varName = p[2]
    indice = p[4]
    if varName in parser.variaveis:
        p[0] = f"PUSHGP\nPUSHI {parser.variaveis[varName][0]}\nPADD\n{indice}LOADN\n"
    else:
        parser.error = (
            f"Variável com o nome {varName} não definida anteriormente.")
        parser.exito = False


# Função que vai buscar o valor do indice na matriz
def p_ProcBusca_Matriz(p):
    "Proc : BUSCA ID ABREPR expr FECHAPR ABREPR expr FECHAPR"
    varName = p[2]
    indice1 = p[4]
    indice2 = p[7]
    if varName in parser.variaveis:
        p[0] = f"PUSHGP\nPUSHI {parser.variaveis[varName][0]}\nPADD\n{indice1}PUSHI {parser.variaveis[varName][2]}\nMUL\nPADD\n{indice2}LOADN\n"
    else:
        parser.error = f"Variável com o nome {varName} não definida"
        parser.exito = False


# Função swap entre elementos do mesmo array
def p_ProcSwap_Lista(p):
    "Proc : SWAP ID ABREPR INT FECHAPR COM ABREPR INT FECHAPR"
    varName = p[2]
    indice1 = p[4]
    indice2 = p[8]
    if varName in parser.variaveis:
        p[0] = f"PUSHG {indice1}\nPUSHG {indice2}\nSTOREG {indice1}\nSTOREG {indice2}\n"
    else:
        parser.error = (
            f"Variável com o nome {varName} não definida anteriormente.")
        parser.exito = False


# Expressão Aritmética Soma
def p_soma(p):
    "exprArit : expr SOMA expr"
    p[0] = f"{p[1]}{p[3]}ADD\n"


# Expressão Aritmética Subtração
def p_sub(p):
    "exprArit : expr MENUS expr"
    p[0] = f"{p[1]}{p[3]}SUB\n"


# Expressão Aritmética Multiplicação
def p_mult(p):
    "exprArit : expr SOMANBEZES expr"
    p[0] = f"{p[1]}{p[3]}MUL\n"


# Expressão Aritmética Divisão
def p_div(p):
    "exprArit : expr DIBIDE expr"
    p[0] = f"{p[1]}{p[3]}MUL\n"


# Expressão Aritmética Resto da divisão
def p_rem(p):
    "exprArit : expr SOBRAS expr"
    p[0] = f"{p[1]}{p[3]}MOD\n"


# Expressão Relativa Não
def p_not(p):
    "exprRel : NOUM ABREPC expr FECHAPC"
    p[0] = f"{p[3]}NOT\n"


# Expressão Relativa Igual
def p_gemeo(p):
    "exprRel : GEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}EQUAL\n"


# Expressão Relativa Diferente
def p_naogemeo(p):
    "exprRel : NAOGEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}NOT\nEQUAL\n"


# Expressão Relativa Menor
def p_inf(p):
    "exprRel : MAISPIQUENO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}INF\n"


# Expressão Relativa Menor ou Igual
def p_infeq(p):
    "exprRel : MAISPIQUENOOUGEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}INFEQ\n"


# Expressão Relativa Maior
def p_sup(p):
    "exprRel : MAISGRANDE ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}SUP\n"


# Expressão Relativa Maior ou Igual
def p_supeq(p):
    "exprRel : MAISGRANDEOUGEMEO ABREPC expr VIRG expr FECHAPC"
    p[0] = f"{p[3]}{p[5]}SUPEQ\n"


# Expressão Relativa E
def p_ie(p):
    "exprRel : expr IE expr"
    p[0] = f"{p[1]}{p[3]}ADD\nPUSHI 2\nEQUAL\n"


# Expressão Relativa OU
def p_oue(p):
    "exprRel : expr OUE expr"
    p[0] = f"{p[1]}{p[3]}ADD\nPUSHI 1\nSUPEQ\n"


# Controlo de fluxo (if then)
def p_if_Then(p):
    "if : SE ABREPC exprRel FECHAPC ENTAO ABRECHAV Corpo FECHACHAV FIM"
    p[0] = f"{p[3]}JZ l{parser.labels}\n{p[7]}l{parser.labels}: NOP\n"
    parser.labels += 1


# Controlo de fluxo (if then else)
def p_if_Then_Else(p):
    "if : SE ABREPC exprRel FECHAPC ENTAO ABRECHAV Corpo FECHACHAV SENAO ABRECHAV Corpo FECHACHAV FIM"
    p[0] = f"{p[3]}JZ l{parser.labels}\n{p[7]}JUMP l{parser.labels}f\nl{parser.labels}: NOP\n{p[11]}l{parser.labels}f: NOP\n"
    parser.labels += 1


# Ciclo (while)
def p_while(p):
    "while : ENQUANTO ABREPC exprRel FECHAPC FAZ ABRECHAV Corpo FECHACHAV FIM"
    p[0] = f'l{parser.labels}c: NOP\n{p[3]}JZ l{parser.labels}f\n{p[7]}JUMP l{parser.labels}c\nl{parser.labels}f: NOP\n'
    parser.labels += 1


def p_saidas_STRING(p):
    "saidas : SAIDAS STRING"
    p[0] = f'PUSHS {p[2]}\nWRITES\n'


def p_saidas_lista(p):
    "saidas : SAIDAS ID"
    if len(parser.variaveis[p[2]])==3 :
        listas = parser.variaveis[p[2]]
        initLista = listas[0]
        numeroListas = listas[1]
        tamanhoListas = listas[2]
        assm = ""
        for i in range(numeroListas):
            for j in range(tamanhoListas):
                assm+=f"PUSHGP\nPUSHI {initLista}\nPADD\nPUSHI {i}\nPUSHI {tamanhoListas}\nPADD\nPUSHI {j}\nLOADN\nWRITEI\n"

    if len(parser.variaveis[p[2]])==2:
        listas = parser.variaveis[p[2]]
        initLista = listas[0]
        tamanhoListas = listas[1]
        assm = ""
        for j in range(tamanhoListas):
            assm+=f"PUSHGP\nPUSHI {initLista}\nPADD\nPUSHI {j}\nLOADN\nWRITEI\n"
        p[0]=assm

def p_saidas_expr(p):
    "saidas : SAIDAS expr"
    p[0] = f"{p[2]}WRITEI\n"


# Funções auxiliares

def p_lista(p):
    "lista : ABREPR elems FECHAPR"
    p[0] = p[2]


def p_elems(p):
    "elems : INT"
    p[0] = [int(p[1])]


def p_elems_rec(p):
    "elems : elems VIRG INT"
    p[0] = p[1]+[p[3]]


# ----------------------------------------

def p_error(p):
    print('Syntax error: ', p, p.type, p.value)
    parser.exito = False

# ----------------------------------------


parser = yacc.yacc(outputdir="./cache")
parser.exito = True
parser.error = ""
parser.assembly = ""
parser.variaveis = {}
parser.stackPointer = 0
parser.linhaDeCodigo = 0
parser.labels = 0

assembly = ""

if len(sys.argv)==3:
    print(f"{sys.argv[0]}, {sys.argv[1]}, {sys.argv[2]}")

if len(sys.argv)==2:
    print(f"{sys.argv[0]}, {sys.argv[1]}")

if len(sys.argv)==1:
    line = input(">")
    while line:
        parser.exito = True
        parser.parse(line)
        if parser.exito:
            assembly += parser.assembly
        else:
            print("--------------------------------------")
            print(parser.error)
            print("--------------------------------------")
            quit
        line = input(">")

    saveMachineCode=input("Do you want to save the code that you generated?[y/n]")
    if saveMachineCode.lower()=="y":
        path = input("Where do you want to save it?")
        if path:
            if ".vm" not in path:
                file = open(f"{path}.vm", "w")
                file.write(assembly)
            else:
                file = open(f"{path}.vm", "w")
                file.write(assembly)
            
        else:
            file = open("./a.vm","w")
            file.write(assembly)

        file.close()
        print("File saved successfully")
        
    else:
        print("Bye Bye")
        quit
