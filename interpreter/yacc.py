# -----------------------------------------------------------------------------
# yacc.py
#
# 2013 10 25 yacc for while language interpreter
# cheyuni_
# -----------------------------------------------------------------------------

# Parsing rules
precedence = (
    ('left', 'AND'),
    ('nonassoc','LT', 'EQUAL'),
    ('left', 'END'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
    ('right', 'UMINUS', 'BANG'),
    )

# syntax tree
        
# def p_statement(t):
#     """statement : statement END statement
#                  """
#     if len(t) == 4:
#         t[0] = [t[1]] + [t[3]] #side effect, assign

def p_statement(t):
    'statement : statement END statement'
    t[0] = [t[1]] + [t[3]] #side effect, assign
        
def p_statement_skip(t):
    'statement : SKIP'
    t[0] = ('SKIP',)
    
# def p_statement_BRACKET(t):
#     'statement : LBRACKET statement RBRACKET'
#     t[0] = t[2]
        
def p_statement_call(t):
    'statement : NAME LPAREN expression RPAREN'
    t[0] = ('FUNCTION_CALL', t[1], t[3])

def p_statement_print(t):
    'statement : PRINT LPAREN expression RPAREN'
    t[0] = ('PRINT', t[3])

def p_statement_if(t):
    """statement : IF LPAREN expression RPAREN LBRACKET statement RBRACKET LBRACKET statement RBRACKET
                 | IF LPAREN expression RPAREN SKIP LBRACKET statement RBRACKET
                 | IF LPAREN expression RPAREN LBRACKET statement RBRACKET SKIP
                 | IF LPAREN expression RPAREN SKIP SKIP
                 """
    if len(t) == 11:
        t[0] = ('IF', t[3], t[6], t[9])
    elif len(t) == 9:
        if t[5] == 'skip':
            t[0] = ('IF', t[3], 'SKIP', t[7])
        else:
            t[0] = ('IF', t[3], t[6], 'SKIP')
    else:
        t[0] = ('IF', t[3], 'SKIP', 'SKIP')

         
def p_statement_while(t):
    'statement : WHILE LPAREN expression RPAREN LBRACKET statement RBRACKET'
    t[0] = ('WHILE', t[3], t[6])
        
def p_statement_proc(t):
    'statement : PROC NAME LPAREN expression RPAREN LBRACKET statement RBRACKET'
    t[0] = ('PROC', t[2], t[4], t[7])
    
    
def p_statement_assign(t):
    """statement : VAR NAME ASSIGN expression 
                 | NAME ASSIGN expression 
                 | VAR NAME 
                 """
    if len(t) == 5:
        t[0] = ("DECLARE_AND_ASSIGN", t[2], t[4])
    elif len(t) == 4:
        t[0] = ("ASSIGN", t[1], t[3])
    else:
        t[0] = ("DECLARE", t[2])

def p_expression_bop(t):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIV expression
                  | expression LT expression
                  | expression AND expression
                  | expression EQUAL expression
                  """
    if(t[2] == '+'):
        t[0] = ('PLUS', t[1], t[3])
    elif(t[2]  == '-'):
        t[0] = ('MINUS', t[1], t[3])
    elif(t[2] == '*'):
        t[0] = ('MUL', t[1], t[3])
    elif(t[2] == '/'):
        t[0] = ('DIVIDE', t[1], t[3])
    elif(t[2] == '<'):
        t[0] = ('LT', t[1], t[3])
    elif(t[2] == '&&'):
        t[0] = ('AND', t[1], t[3])
    else:
        t[0] = ('EQUAL', t[1], t[3])

def p_expression_paren(t):
    """expression : LPAREN expression RPAREN"""
    t[0] = t[2]
    
        
def p_expression_uop(t):
    """expression : MINUS expression %prec UMINUS
                  | BANG expression
    """
    if(t[1] == '-'):
        t[0] = ("UMINUS", t[2])
    else:
        t[0] = ("BANG", t[2])
        
        
def p_expression_int(t):
    'expression : INT'
    t[0] = ('INT', t[1])

def p_expression_var(t):
    'expression : NAME'
    t[0] = ('NAME', t[1])


def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()
