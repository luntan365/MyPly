
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLTLEGTGEEQNEleftREMADDleftMULDIVMODleftPOWNUMBER ID SPLIT STRING TRUE FALSE PRINT AND OR IF ADD REM MUL DIV MOD LT GT LPAREN RPAREN ASSIGN COMMA COLON GE LE EQ NE POWstart : function\n    function : function statement SPLIT\n             | function line_statement\n             | empty\n    line_statement : SPLITline_statement : expression SPLIT\n    statement : PRINT LPAREN expr_list RPAREN\n    \n    line_statement : IF condition_list COLON statement SPLIT\n                   | IF condition_list COLON SPLIT statement SPLIT\n    \n    line_statement : ID ASSIGN expression SPLIT\n                   | ID ASSIGN condition_list SPLIT\n    \n    expr_list : expression\n              | expr_list COMMA expression\n    \n    condition_list : expression\n                   | condition_list AND expression\n                   | condition_list OR expression\n    condition_list : LPAREN condition_list RPARENexpression : TRUEexpression : FALSEexpression : IDexpression : NUMBERexpression : STRING\n    expression : expression ADD expression\n               | expression REM expression\n               | expression MUL expression\n               | expression DIV expression\n               | expression MOD expression\n               | expression GT expression\n               | expression LT expression\n               | expression GE expression\n               | expression LE expression\n               | expression EQ expression\n               | expression NE expression\n               | expression POW expression\n    expression : LPAREN expression RPARENempty :'
    
_lr_action_items = {'PRINT':([0,2,3,5,6,16,20,52,63,67,68,71,73,],[-36,7,-4,-5,-3,-2,-6,7,7,-10,-11,-8,-9,]),'SPLIT':([0,2,3,4,5,6,9,11,12,13,14,15,16,19,20,39,40,41,42,43,44,45,46,47,48,49,50,51,52,57,58,60,62,64,65,66,67,68,71,72,73,],[-36,5,-4,16,-5,-3,20,-20,-18,-19,-21,-22,-2,-20,-6,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,63,67,68,-7,71,-15,-16,-17,-10,-11,-8,73,-9,]),'IF':([0,2,3,5,6,16,20,67,68,71,73,],[-36,10,-4,-5,-3,-2,-6,-10,-11,-8,-9,]),'ID':([0,2,3,5,6,8,10,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,35,36,53,54,59,61,67,68,71,73,],[-36,11,-4,-5,-3,19,19,-2,19,-6,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-10,-11,-8,-9,]),'TRUE':([0,2,3,5,6,8,10,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,35,36,53,54,59,61,67,68,71,73,],[-36,12,-4,-5,-3,12,12,-2,12,-6,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-10,-11,-8,-9,]),'FALSE':([0,2,3,5,6,8,10,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,35,36,53,54,59,61,67,68,71,73,],[-36,13,-4,-5,-3,13,13,-2,13,-6,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-10,-11,-8,-9,]),'NUMBER':([0,2,3,5,6,8,10,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,35,36,53,54,59,61,67,68,71,73,],[-36,14,-4,-5,-3,14,14,-2,14,-6,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-10,-11,-8,-9,]),'STRING':([0,2,3,5,6,8,10,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,35,36,53,54,59,61,67,68,71,73,],[-36,15,-4,-5,-3,15,15,-2,15,-6,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-10,-11,-8,-9,]),'LPAREN':([0,2,3,5,6,7,8,10,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,35,36,53,54,59,61,67,68,71,73,],[-36,8,-4,-5,-3,17,8,35,-2,8,-6,8,8,8,8,8,8,8,8,8,8,8,8,35,59,8,8,59,8,-10,-11,-8,-9,]),'$end':([0,1,2,3,5,6,16,20,67,68,71,73,],[-36,0,-1,-4,-5,-3,-2,-6,-10,-11,-8,-9,]),'ADD':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[21,-20,-18,-19,-21,-22,21,-20,21,21,-35,-23,-24,-25,-26,-27,21,21,21,21,21,21,-34,21,21,21,21,21,21,]),'REM':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[22,-20,-18,-19,-21,-22,22,-20,22,22,-35,-23,-24,-25,-26,-27,22,22,22,22,22,22,-34,22,22,22,22,22,22,]),'MUL':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[23,-20,-18,-19,-21,-22,23,-20,23,23,-35,23,23,-25,-26,-27,23,23,23,23,23,23,-34,23,23,23,23,23,23,]),'DIV':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[24,-20,-18,-19,-21,-22,24,-20,24,24,-35,24,24,-25,-26,-27,24,24,24,24,24,24,-34,24,24,24,24,24,24,]),'MOD':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[25,-20,-18,-19,-21,-22,25,-20,25,25,-35,25,25,-25,-26,-27,25,25,25,25,25,25,-34,25,25,25,25,25,25,]),'GT':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[26,-20,-18,-19,-21,-22,26,-20,26,26,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,26,26,26,26,26,26,]),'LT':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[27,-20,-18,-19,-21,-22,27,-20,27,27,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,27,27,27,27,27,27,]),'GE':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[28,-20,-18,-19,-21,-22,28,-20,28,28,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,28,28,28,28,28,28,]),'LE':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[29,-20,-18,-19,-21,-22,29,-20,29,29,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,29,29,29,29,29,29,]),'EQ':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[30,-20,-18,-19,-21,-22,30,-20,30,30,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,30,30,30,30,30,30,]),'NE':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[31,-20,-18,-19,-21,-22,31,-20,31,31,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,31,31,31,31,31,31,]),'POW':([9,11,12,13,14,15,18,19,34,38,39,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,],[32,-20,-18,-19,-21,-22,32,-20,32,32,-35,32,32,32,32,32,32,32,32,32,32,32,-34,32,32,32,32,32,32,]),'ASSIGN':([11,],[36,]),'RPAREN':([12,13,14,15,18,19,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,55,56,64,65,66,69,70,],[-18,-19,-21,-22,39,-20,60,-12,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,66,39,-15,-16,-17,39,-13,]),'COLON':([12,13,14,15,19,33,34,39,40,41,42,43,44,45,46,47,48,49,50,51,64,65,66,],[-18,-19,-21,-22,-20,52,-14,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-15,-16,-17,]),'AND':([12,13,14,15,19,33,34,39,40,41,42,43,44,45,46,47,48,49,50,51,55,56,57,58,64,65,66,69,],[-18,-19,-21,-22,-20,53,-14,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,53,-14,-14,53,-15,-16,-17,-14,]),'OR':([12,13,14,15,19,33,34,39,40,41,42,43,44,45,46,47,48,49,50,51,55,56,57,58,64,65,66,69,],[-18,-19,-21,-22,-20,54,-14,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,54,-14,-14,54,-15,-16,-17,-14,]),'COMMA':([12,13,14,15,19,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,70,],[-18,-19,-21,-22,-20,61,-12,-35,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'function':([0,],[2,]),'empty':([0,],[3,]),'statement':([2,52,63,],[4,62,72,]),'line_statement':([2,],[6,]),'expression':([2,8,10,17,21,22,23,24,25,26,27,28,29,30,31,32,35,36,53,54,59,61,],[9,18,34,38,40,41,42,43,44,45,46,47,48,49,50,51,56,57,64,65,69,70,]),'condition_list':([10,35,36,59,],[33,55,58,55,]),'expr_list':([17,],[37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> function','start',1,'p_start','dparser.py',45),
  ('function -> function statement SPLIT','function',3,'p_function','dparser.py',51),
  ('function -> function line_statement','function',2,'p_function','dparser.py',52),
  ('function -> empty','function',1,'p_function','dparser.py',53),
  ('line_statement -> SPLIT','line_statement',1,'p_statement_none','dparser.py',61),
  ('line_statement -> expression SPLIT','line_statement',2,'p_statement_expr','dparser.py',65),
  ('statement -> PRINT LPAREN expr_list RPAREN','statement',4,'p_statement_print','dparser.py',72),
  ('line_statement -> IF condition_list COLON statement SPLIT','line_statement',5,'p_statement_cond','dparser.py',80),
  ('line_statement -> IF condition_list COLON SPLIT statement SPLIT','line_statement',6,'p_statement_cond','dparser.py',81),
  ('line_statement -> ID ASSIGN expression SPLIT','line_statement',4,'p_statement_assign','dparser.py',92),
  ('line_statement -> ID ASSIGN condition_list SPLIT','line_statement',4,'p_statement_assign','dparser.py',93),
  ('expr_list -> expression','expr_list',1,'p_expression_list','dparser.py',101),
  ('expr_list -> expr_list COMMA expression','expr_list',3,'p_expression_list','dparser.py',102),
  ('condition_list -> expression','condition_list',1,'p_condition_list','dparser.py',112),
  ('condition_list -> condition_list AND expression','condition_list',3,'p_condition_list','dparser.py',113),
  ('condition_list -> condition_list OR expression','condition_list',3,'p_condition_list','dparser.py',114),
  ('condition_list -> LPAREN condition_list RPAREN','condition_list',3,'p_condition_parens','dparser.py',125),
  ('expression -> TRUE','expression',1,'p_expression_true','dparser.py',131),
  ('expression -> FALSE','expression',1,'p_expression_false','dparser.py',137),
  ('expression -> ID','expression',1,'p_expression_var','dparser.py',143),
  ('expression -> NUMBER','expression',1,'p_expression_num','dparser.py',149),
  ('expression -> STRING','expression',1,'p_expression_string','dparser.py',155),
  ('expression -> expression ADD expression','expression',3,'p_expression_two_operator','dparser.py',162),
  ('expression -> expression REM expression','expression',3,'p_expression_two_operator','dparser.py',163),
  ('expression -> expression MUL expression','expression',3,'p_expression_two_operator','dparser.py',164),
  ('expression -> expression DIV expression','expression',3,'p_expression_two_operator','dparser.py',165),
  ('expression -> expression MOD expression','expression',3,'p_expression_two_operator','dparser.py',166),
  ('expression -> expression GT expression','expression',3,'p_expression_two_operator','dparser.py',167),
  ('expression -> expression LT expression','expression',3,'p_expression_two_operator','dparser.py',168),
  ('expression -> expression GE expression','expression',3,'p_expression_two_operator','dparser.py',169),
  ('expression -> expression LE expression','expression',3,'p_expression_two_operator','dparser.py',170),
  ('expression -> expression EQ expression','expression',3,'p_expression_two_operator','dparser.py',171),
  ('expression -> expression NE expression','expression',3,'p_expression_two_operator','dparser.py',172),
  ('expression -> expression POW expression','expression',3,'p_expression_two_operator','dparser.py',173),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_parens','dparser.py',180),
  ('empty -> <empty>','empty',0,'p_empty','dparser.py',190),
]
