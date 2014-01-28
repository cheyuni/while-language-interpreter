
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xa7b\x8c\xb2\x18e\xb7\\3\x86\xe0!V.\xc4\x9f'
    
_lr_action_items = {'EQUAL':([17,18,21,23,26,28,29,30,31,40,41,42,46,47,48,49,50,51,52,53,],[-25,-24,34,34,34,34,34,-23,34,-22,34,34,-21,34,None,None,-14,-16,-17,-15,]),'LBRACKET':([43,45,54,56,66,],[55,57,58,61,70,]),'WHILE':([0,14,55,57,58,61,70,],[5,5,5,5,5,5,5,]),'PRINT':([0,14,55,57,58,61,70,],[7,7,7,7,7,7,7,]),'MUL':([17,18,21,23,26,28,29,30,31,40,41,42,46,47,48,49,50,51,52,53,],[-25,-24,37,37,37,37,37,-23,37,-22,37,37,-21,37,37,37,37,-16,-17,37,]),'DIV':([17,18,21,23,26,28,29,30,31,40,41,42,46,47,48,49,50,51,52,53,],[-25,-24,38,38,38,38,38,-23,38,-22,38,38,-21,38,38,38,38,-16,-17,38,]),'MINUS':([9,10,13,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,34,35,36,37,38,39,40,41,42,46,47,48,49,50,51,52,53,],[22,22,22,22,22,-25,-24,22,22,39,22,39,22,22,39,39,39,-23,39,22,22,22,22,22,22,22,-22,39,39,-21,39,39,39,-14,-16,-17,-15,]),'RPAREN':([17,18,21,26,28,29,30,31,40,41,46,47,48,49,50,51,52,53,],[-25,-24,33,43,44,45,-23,46,-22,54,-21,-19,-20,-18,-14,-16,-17,-15,]),'LT':([17,18,21,23,26,28,29,30,31,40,41,42,46,47,48,49,50,51,52,53,],[-25,-24,35,35,35,35,35,-23,35,-22,35,35,-21,35,None,None,-14,-16,-17,-15,]),'PLUS':([17,18,21,23,26,28,29,30,31,40,41,42,46,47,48,49,50,51,52,53,],[-25,-24,36,36,36,36,36,-23,36,-22,36,36,-21,36,36,36,-14,-16,-17,-15,]),'ASSIGN':([1,12,],[10,25,]),'$end':([2,6,12,17,18,23,27,30,33,40,42,44,46,47,48,49,50,51,52,53,60,64,67,68,69,72,],[-2,0,-13,-25,-24,-12,-1,-23,-3,-22,-11,-4,-21,-19,-20,-18,-14,-16,-17,-15,-8,-9,-10,-6,-7,-5,]),'END':([2,6,12,17,18,23,27,30,33,40,42,44,46,47,48,49,50,51,52,53,59,60,62,63,64,65,67,68,69,71,72,],[-2,14,-13,-25,-24,-12,-1,-23,-3,-22,-11,-4,-21,-19,-20,-18,-14,-16,-17,-15,14,-8,14,14,-9,14,-10,-6,-7,14,-5,]),'SKIP':([0,14,45,55,56,57,58,61,66,70,],[2,2,56,2,60,2,2,2,69,2,]),'BANG':([9,10,13,15,16,19,20,22,24,25,32,34,35,36,37,38,39,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'LPAREN':([1,5,7,8,9,10,11,13,15,16,19,20,22,24,25,32,34,35,36,37,38,39,],[9,13,15,16,20,20,24,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'VAR':([0,14,55,57,58,61,70,],[4,4,4,4,4,4,4,]),'IF':([0,14,55,57,58,61,70,],[8,8,8,8,8,8,8,]),'AND':([17,18,21,23,26,28,29,30,31,40,41,42,46,47,48,49,50,51,52,53,],[-25,-24,32,32,32,32,32,-23,32,-22,32,32,-21,-19,-20,-18,-14,-16,-17,-15,]),'NAME':([0,3,4,9,10,13,14,15,16,19,20,22,24,25,32,34,35,36,37,38,39,55,57,58,61,70,],[1,11,12,17,17,17,1,17,17,17,17,17,17,17,17,17,17,17,17,17,17,1,1,1,1,1,]),'INT':([9,10,13,15,16,19,20,22,24,25,32,34,35,36,37,38,39,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'RBRACKET':([2,12,17,18,23,27,30,33,40,42,44,46,47,48,49,50,51,52,53,59,60,62,63,64,65,67,68,69,71,72,],[-2,-13,-25,-24,-12,-1,-23,-3,-22,-11,-4,-21,-19,-20,-18,-14,-16,-17,-15,64,-8,66,67,-9,68,-10,-6,-7,72,-5,]),'PROC':([0,14,55,57,58,61,70,],[3,3,3,3,3,3,3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([9,10,13,15,16,19,20,22,24,25,32,34,35,36,37,38,39,],[21,23,26,28,29,30,31,40,41,42,47,48,49,50,51,52,53,]),'statement':([0,14,55,57,58,61,70,],[6,27,59,62,63,65,71,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> statement END statement','statement',3,'p_statement','/tmp/py19512pJb',113),
  ('statement -> SKIP','statement',1,'p_statement_skip','/tmp/py19512pJb',117),
  ('statement -> NAME LPAREN expression RPAREN','statement',4,'p_statement_call','/tmp/py19512pJb',125),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_print','/tmp/py19512pJb',129),
  ('statement -> IF LPAREN expression RPAREN LBRACKET statement RBRACKET LBRACKET statement RBRACKET','statement',10,'p_statement_if','/tmp/py19512pJb',133),
  ('statement -> IF LPAREN expression RPAREN SKIP LBRACKET statement RBRACKET','statement',8,'p_statement_if','/tmp/py19512pJb',134),
  ('statement -> IF LPAREN expression RPAREN LBRACKET statement RBRACKET SKIP','statement',8,'p_statement_if','/tmp/py19512pJb',135),
  ('statement -> IF LPAREN expression RPAREN SKIP SKIP','statement',6,'p_statement_if','/tmp/py19512pJb',136),
  ('statement -> WHILE LPAREN expression RPAREN LBRACKET statement RBRACKET','statement',7,'p_statement_while','/tmp/py19512pJb',150),
  ('statement -> PROC NAME LPAREN expression RPAREN LBRACKET statement RBRACKET','statement',8,'p_statement_proc','/tmp/py19512pJb',154),
  ('statement -> VAR NAME ASSIGN expression','statement',4,'p_statement_assign','/tmp/py19512pJb',159),
  ('statement -> NAME ASSIGN expression','statement',3,'p_statement_assign','/tmp/py19512pJb',160),
  ('statement -> VAR NAME','statement',2,'p_statement_assign','/tmp/py19512pJb',161),
  ('expression -> expression PLUS expression','expression',3,'p_expression_bop','/tmp/py19512pJb',171),
  ('expression -> expression MINUS expression','expression',3,'p_expression_bop','/tmp/py19512pJb',172),
  ('expression -> expression MUL expression','expression',3,'p_expression_bop','/tmp/py19512pJb',173),
  ('expression -> expression DIV expression','expression',3,'p_expression_bop','/tmp/py19512pJb',174),
  ('expression -> expression LT expression','expression',3,'p_expression_bop','/tmp/py19512pJb',175),
  ('expression -> expression AND expression','expression',3,'p_expression_bop','/tmp/py19512pJb',176),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_bop','/tmp/py19512pJb',177),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','/tmp/py19512pJb',195),
  ('expression -> MINUS expression','expression',2,'p_expression_uop','/tmp/py19512pJb',200),
  ('expression -> BANG expression','expression',2,'p_expression_uop','/tmp/py19512pJb',201),
  ('expression -> INT','expression',1,'p_expression_int','/tmp/py19512pJb',210),
  ('expression -> NAME','expression',1,'p_expression_var','/tmp/py19512pJb',214),
]