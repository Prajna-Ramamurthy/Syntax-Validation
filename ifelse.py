tokens = ('NAME', 'INT', 'DOUBLE', 'GREATER', 'LESS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'LPAREN', 'RPAREN', 'CHAR', 'TRUE', 'FALSE', 'GREATEQ', 'LESSEQ', 'EQEQ', 'NOTEQ', 'AND', 'OR', 'COLON', 'IF', 'ELSE')

# Reserved words
reserved = {'if' : 'IF', 'else' : 'ELSE'}

# Tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_CHAR    = r'\'[a-zA-Z0-9_+\*\- :,\s]*\''
t_TRUE    = r'\t'
t_FALSE   = r'\f'
t_GREATER = r'>'
t_LESS    = r'<'
t_GREATEQ = r'>='
t_LESSEQ  = r'<='
t_EQEQ    = r'=='
t_NOTEQ   = r'!='
t_AND     = r'&'
t_OR      = r'\|'
t_COLON   = r':'

def t_DOUBLE(t):
    r'[0-9]+\.[0-9]+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_INT(t):
    r'[0-9]+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Double value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules
precedence = (
    ('left','AND','OR'),
    ('left','GREATER','LESS', 'GREATEQ', 'LESSEQ', 'EQEQ', 'NOTEQ'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS')
    )

# dictionary of names
names = { }

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_statement_if(t):
    'statement : IF LPAREN expression RPAREN COLON statement'
    pass

def p_statement_else(t):
    'statement : IF LPAREN expression RPAREN COLON statement ELSE COLON statement '
    pass

def p_expression_ariop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_logop(t):
    '''expression : expression GREATER expression
                  | expression LESS expression
                  | expression GREATEQ expression
                  | expression LESSEQ expression
                  | expression EQEQ expression
                  | expression NOTEQ expression
                  | expression AND expression
                  | expression OR expression'''


    if t[2] == '>'  : t[0] = t[1] > t[3]
    elif t[2] == '<': t[0] = t[1] < t[3]
    elif t[2] == '>=': t[0] = t[1] >= t[3]
    elif t[2] == '<=': t[0] = t[1] <= t[3]
    elif t[2] == '==': t[0] = t[1] == t[3]
    elif t[2] == '!=': t[0] = t[1] != t[3]
    elif t[2] == '&': t[0] = t[1] and t[3]
    elif t[2] == '|': t[0] = t[1] or t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_int(t):
    'expression : INT'
    t[0] = t[1]

def p_expression_double(t):
    'expression : DOUBLE'
    t[0] = t[1]

def p_expression_char(t):
    'expression : CHAR'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        t[0] = 0

def p_expression_bool(t):
    'expression : bool'
    t[0] = t[1]


def p_true(t):
    'bool : TRUE'
    t[0] = True

def p_false(t):
    'bool : FALSE'
    t[0] = False

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

# input file containing the Python if else code
print("Reading input from text file... \n")
myFile = open("input.txt","r+")
inputFile = myFile.read()
print(inputFile)
parser.parse(inputFile)
print("Grammar has been verified...")
