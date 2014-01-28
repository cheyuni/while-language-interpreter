# -----------------------------------------------------------------------------
# lex.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

reserved = {
   'if' : 'IF',
   'skip' : 'SKIP',
   'while' : 'WHILE',
   'var' : 'VAR',
   'proc' : 'PROC',
}

tokens = [
    'INT', 'NAME',
    'UOP', 'BOP',
    'EXPR', 'STMT',
    'END', 'EQUALS',
    'LPAREN','RPAREN',
    'LBRACKET','RBRACKET',    
    ] + list(reserved.values())

t_INT = r'-?[0-9]+'
t_NAME = r'[a-zA-Z][a-zA-Z0-9]*'
t_UOP = r'[\!\-]'
t_BOP = r'(==|&&|[\+\-\*\/\<])'
t_END = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_EQUALS = r'\='

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

def t_INT(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
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

# Parsing rules

# precedence = (
#     ('left','PLUS','MINUS'),
#     ('left','TIMES','DIVIDE'),
#     ('right','UMINUS'),
#     )
# # dictionary of names
# names = { }

# def p_statement_assign(t):
#     'statement : NAME EQUALS expression'
#     names[t[1]] = t[3]

# def p_statement_expr(t):
#     'statement : expression'
#     print(t[1])

# def p_expression_binop(t):
#     '''expression : expression PLUS expression
#     | expression MINUS expression
#     | expression TIMES expression
#     | expression DIVIDE expression'''
#     if t[2] == '+'  : t[0] = t[1] + t[3]
#     elif t[2] == '-': t[0] = t[1] - t[3]
#     elif t[2] == '*': t[0] = t[1] * t[3]
#     elif t[2] == '/': t[0] = t[1] / t[3]

# def p_expression_uminus(t):
#     'expression : MINUS expression %prec UMINUS'
#     t[0] = -t[2]

# def p_expression_group(t):
#     'expression : LPAREN expression RPAREN'
#     t[0] = t[2]

# def p_expression_number(t):
#     'expression : NUMBER'
#     t[0] = t[1]

# def p_expression_name(t):
#     'expression : NAME'
#     try:
#         t[0] = names[t[1]]
#     except LookupError:
#         print("Undefined name '%s'" % t[1])
#         t[0] = 0

# def p_error(t):
#     print("Syntax error at '%s'" % t.value)

# import ply.yacc as yacc
# yacc.yacc()


s = """
var ret;
proc fib(n) {
var tmp;
ret = 1;
tmp = -1;
while (!(n==1) && !(n==2)) {
var local;
local = ret - tmp;
tmp = - ret;
ret = local;
n = n - 1
}
}
proc sum(n) {
if (n<1)
skip
{ sum(n-1); ret = ret + n }
}
if (in<1)
skip
{
sum(in);
fib(ret);
print(ret)
}
"""
lex.input(s)
while 1:
    tok = lex.token()
    if not tok :
        break
    print tok;

# while 1:
#     try:
#         s = raw_input('calc > ')   # Use raw_input on Python 2
#     except EOFError:
#         break
#     yacc.parse(s)
#     lex.input(s)
#     while 1:
#         tok = lex.token()
#         if not tok :
#             break
#         print tok;
#     yacc.parse(s, lex)



