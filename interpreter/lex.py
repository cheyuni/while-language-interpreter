# -----------------------------------------------------------------------------
# lex.py
#
# 2013 10 25 lexer for while language interpreter
# cheyuni_
# -----------------------------------------------------------------------------

reserved = {
   'if' : 'IF',
   'skip' : 'SKIP',
   'while' : 'WHILE',
   'var' : 'VAR',
   'proc' : 'PROC',
   'print' : 'PRINT',
}

tokens = [
    'INT', 'NAME',
    'BANG', 'LT',
    'MINUS', 'PLUS',
    'MUL', 'DIV',
    'EQUAL', 'AND',    
    'END', 'ASSIGN', 
    'LPAREN','RPAREN',
    'LBRACKET','RBRACKET',
    ] + list(reserved.values())

t_INT = r'[0-9]+'
t_NAME = r'[a-zA-Z][a-zA-Z0-9]*'
t_BANG = r'\!'
t_MINUS = r'\-'
t_PLUS = r'\+'
t_MUL = r'\*'
t_LT = r'\<'
t_DIV = r'/'
t_EQUAL = r'\=\='
t_AND = r'\&\&'
t_END = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_ASSIGN = r'\='

# Tokens

def t_IF(t):
    r'if'
    t.type = reserved.get(t.value,'IF')
    return t

def t_SKIP(t):
    r'skip'
    t.type = reserved.get(t.value,'SKIP')
    return t

def t_WHILE(t):
    r'while'
    t.type = reserved.get(t.value,'WHILE')
    return t

def t_PROC(t):
    r'proc'
    t.type = reserved.get(t.value,'PROC')
    return t

def t_VAR(t):
    r'var'
    t.type = reserved.get(t.value,'VAR')
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r' \n'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

