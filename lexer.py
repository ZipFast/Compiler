import re

GTEQ = ">="
LTEQ = "<="
ARROW = "-->"
PLUS = "+"
MINUS = "-"
SLASH = "/"
ASSIGN = "="
SEMI = ";"
COMMA = ","
LPAR = "("
RPAR = ")"
LT = "<"
GT = ">"
IF = "if"
DEF = "def"
ELSE = "else"
FI = "fi"
WHILE = "while"
IDENT = "IDENT"
NUMBERAL = "NUMERAL"
ERROR = "ERROR"
STAR = "*"
_tokenMap = {
        GTEQ: GTEQ, LTEQ: LTEQ, ARROW: ARROW, GT: GT, LT: LT,
        PLUS: PLUS, MINUS: MINUS, STAR: STAR, SLASH: SLASH, ASSIGN: ASSIGN,
        LPAR: LPAR, RPAR: RPAR, SEMI: SEMI, COMMA: COMMA,
        IF: IF, DEF: DEF, ELSE: ELSE, FI: FI, WHILE: WHILE }

def readTokens(file):
    """ A generator that return pairs (C, L) consisting of
    the lexemes in FILE (L) and their syntactic categories (C). """

    for token in re.finditer(r"(\s+|#.*)"
                             r"|>=|<=|-->|if|def|else|fi|while"
                             r"|([a-zA-z][a-zA-z0-9]*)|(\d+)"
                             r"|.",
                             file.read()):
        L = token.group(0)
        i = token.lastindex
        # space and comment
        if i == 1:
            pass
        elif i == 2:
            yield IDENT, L
        elif i == 3:
            yield NUMBERAL, L
        else:
            yield _tokenMap.get(L, ERROR), L

file = open("test.cl", "r")
for C, L in readTokens(file):
    print(C)
