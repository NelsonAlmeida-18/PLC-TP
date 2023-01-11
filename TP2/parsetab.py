
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRECHAV ABREPC ABREPR ALTERNA BUSCA COM DIBIDE ENQUANTO ENTAO ENTRADAS FAZ FECHACHAV FECHAPC FECHAPR FIM GEMEO ID IE INT LISTA MAISGRANDE MAISGRANDEOUGEMEO MAISPIQUENO MAISPIQUENOOUGEMEO MATRIZ MENUS NAOGEMEO NOUM OUE SAIDAS SE SENAO SOBRAS SOMA SOMANBEZES VAR VIRG\n    Programa : Decls\n             | Atrib\n    \n    Programa : Decls Corpo\n    \n    Programa : Corpo\n    \n    Corpo : Proc\n          | Atrib\n    \n    Corpo : Proc Corpo\n          | Atrib Corpo\n    Decls : DeclDecls : Decls Decl\n    expr : exprArit\n         | exprRel\n    \n    Proc : if\n         | while\n         | saidas\n    Decl : VAR IDAtrib : VAR ID COM exprAtrib : ALTERNA ID COM exprDecl : LISTA IDDecl : LISTA ID INTAtrib : ALTERNA ID ABREPR expr FECHAPR ABREPR expr FECHAPR COM exprAtrib : ALTERNA ID ABREPR expr FECHAPR COM listaAtrib : ALTERNA ID ABREPR expr FECHAPR COM exprAtrib : LISTA ID COM listaDecl : MATRIZ IDDecl : MATRIZ ID INT INTProc : BUSCA ID ABREPR expr FECHAPRexprArit : expr SOMA exprexprArit : expr MENUS exprexprArit : expr SOMANBEZES exprexprArit : expr DIBIDE exprexprArit : expr SOBRAS exprexprRel : NOUM ABREPC expr FECHAPCexprRel : GEMEO ABREPC expr VIRG expr FECHAPCexprRel : NAOGEMEO ABREPC expr VIRG expr FECHAPCexprRel : MAISPIQUENO ABREPC expr VIRG expr FECHAPCexprRel : MAISPIQUENOOUGEMEO ABREPC expr VIRG expr FECHAPCexprRel : MAISGRANDE ABREPC expr VIRG expr FECHAPCexprRel : MAISGRANDEOUGEMEO ABREPC expr VIRG expr FECHAPCexprRel : expr IE exprexprRel : expr OUE exprif : SE ABREPC exprRel FECHAPC ENTAO ABRECHAV Corpo FECHACHAV SENAO ABRECHAV Corpo FECHACHAV FIMif : SE ABREPC exprRel FECHAPC ENTAO ABRECHAV Corpo FECHACHAV FIMwhile : ENQUANTO ABREPC exprRel FECHAPC FAZ ABRECHAV Corpo FECHACHAV FIMexpr : ENTRADASexpr : INTexpr : IDlista : ABREPR elems FECHAPRelems : INTelems : elems VIRG INTProc : BUSCA ID ABREPR expr FECHAPR ABREPR expr FECHAPRsaidas : SAIDAS IDsaidas : SAIDAS expr'
    
_lr_action_items = {'VAR':([0,2,3,5,9,11,12,13,19,20,26,28,30,34,35,36,37,38,39,47,48,55,60,76,77,79,81,85,86,87,88,89,90,91,102,105,114,117,118,126,127,132,133,134,135,136,137,139,144,145,146,147,150,],[6,21,24,-9,24,-13,-14,-15,-10,24,-16,-19,-25,-47,-53,-11,-12,-45,-46,-16,-19,-20,-47,-17,-18,-24,-26,-28,-29,-30,-31,-32,-40,-41,-27,-33,-48,24,24,-23,-22,-34,-35,-36,-37,-38,-39,-51,-43,-44,-21,24,-42,]),'ALTERNA':([0,2,3,5,9,11,12,13,19,20,26,28,30,34,35,36,37,38,39,47,48,55,60,76,77,79,81,85,86,87,88,89,90,91,102,105,114,117,118,126,127,132,133,134,135,136,137,139,144,145,146,147,150,],[7,7,7,-9,7,-13,-14,-15,-10,7,-16,-19,-25,-47,-53,-11,-12,-45,-46,-16,-19,-20,-47,-17,-18,-24,-26,-28,-29,-30,-31,-32,-40,-41,-27,-33,-48,7,7,-23,-22,-34,-35,-36,-37,-38,-39,-51,-43,-44,-21,7,-42,]),'LISTA':([0,2,3,5,9,11,12,13,19,20,26,28,30,34,35,36,37,38,39,47,48,55,60,76,77,79,81,85,86,87,88,89,90,91,102,105,114,117,118,126,127,132,133,134,135,136,137,139,144,145,146,147,150,],[8,22,25,-9,25,-13,-14,-15,-10,25,-16,-19,-25,-47,-53,-11,-12,-45,-46,-16,-19,-20,-47,-17,-18,-24,-26,-28,-29,-30,-31,-32,-40,-41,-27,-33,-48,25,25,-23,-22,-34,-35,-36,-37,-38,-39,-51,-43,-44,-21,25,-42,]),'MATRIZ':([0,2,5,19,26,28,30,47,48,55,81,],[10,10,-9,-10,-16,-19,-25,-16,-19,-20,-26,]),'BUSCA':([0,2,3,5,9,11,12,13,19,20,26,28,30,34,35,36,37,38,39,47,48,55,60,76,77,79,81,85,86,87,88,89,90,91,102,105,114,117,118,126,127,132,133,134,135,136,137,139,144,145,146,147,150,],[14,14,14,-9,14,-13,-14,-15,-10,14,-16,-19,-25,-47,-53,-11,-12,-45,-46,-16,-19,-20,-47,-17,-18,-24,-26,-28,-29,-30,-31,-32,-40,-41,-27,-33,-48,14,14,-23,-22,-34,-35,-36,-37,-38,-39,-51,-43,-44,-21,14,-42,]),'SE':([0,2,3,5,9,11,12,13,19,20,26,28,30,34,35,36,37,38,39,47,48,55,60,76,77,79,81,85,86,87,88,89,90,91,102,105,114,117,118,126,127,132,133,134,135,136,137,139,144,145,146,147,150,],[15,15,15,-9,15,-13,-14,-15,-10,15,-16,-19,-25,-47,-53,-11,-12,-45,-46,-16,-19,-20,-47,-17,-18,-24,-26,-28,-29,-30,-31,-32,-40,-41,-27,-33,-48,15,15,-23,-22,-34,-35,-36,-37,-38,-39,-51,-43,-44,-21,15,-42,]),'ENQUANTO':([0,2,3,5,9,11,12,13,19,20,26,28,30,34,35,36,37,38,39,47,48,55,60,76,77,79,81,85,86,87,88,89,90,91,102,105,114,117,118,126,127,132,133,134,135,136,137,139,144,145,146,147,150,],[16,16,16,-9,16,-13,-14,-15,-10,16,-16,-19,-25,-47,-53,-11,-12,-45,-46,-16,-19,-20,-47,-17,-18,-24,-26,-28,-29,-30,-31,-32,-40,-41,-27,-33,-48,16,16,-23,-22,-34,-35,-36,-37,-38,-39,-51,-43,-44,-21,16,-42,]),'SAIDAS':([0,2,3,5,9,11,12,13,19,20,26,28,30,34,35,36,37,38,39,47,48,55,60,76,77,79,81,85,86,87,88,89,90,91,102,105,114,117,118,126,127,132,133,134,135,136,137,139,144,145,146,147,150,],[17,17,17,-9,17,-13,-14,-15,-10,17,-16,-19,-25,-47,-53,-11,-12,-45,-46,-16,-19,-20,-47,-17,-18,-24,-26,-28,-29,-30,-31,-32,-40,-41,-27,-33,-48,17,17,-23,-22,-34,-35,-36,-37,-38,-39,-51,-43,-44,-21,17,-42,]),'$end':([1,2,3,4,5,9,11,12,13,18,19,20,23,26,28,29,30,34,35,36,37,38,39,47,48,55,60,76,77,79,81,85,86,87,88,89,90,91,102,105,114,126,127,132,133,134,135,136,137,139,144,145,146,150,],[0,-1,-2,-4,-9,-5,-13,-14,-15,-3,-10,-6,-8,-16,-19,-7,-25,-47,-53,-11,-12,-45,-46,-16,-19,-20,-47,-17,-18,-24,-26,-28,-29,-30,-31,-32,-40,-41,-27,-33,-48,-23,-22,-34,-35,-36,-37,-38,-39,-51,-43,-44,-21,-42,]),'ID':([6,7,8,10,14,17,21,22,24,25,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[26,27,28,30,31,34,47,48,49,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'FECHACHAV':([9,11,12,13,20,23,29,34,35,36,37,38,39,60,76,77,79,85,86,87,88,89,90,91,102,105,114,126,127,130,131,132,133,134,135,136,137,139,144,145,146,148,150,],[-5,-13,-14,-15,-6,-8,-7,-47,-53,-11,-12,-45,-46,-47,-17,-18,-24,-28,-29,-30,-31,-32,-40,-41,-27,-33,-48,-23,-22,140,141,-34,-35,-36,-37,-38,-39,-51,-43,-44,-21,149,-42,]),'ABREPC':([15,16,40,41,42,43,44,45,46,],[32,33,69,70,71,72,73,74,75,]),'ENTRADAS':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'INT':([17,28,30,32,33,48,51,52,53,56,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,80,106,107,108,109,110,111,112,113,115,116,142,],[39,55,56,39,39,55,39,39,39,81,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,101,39,39,39,39,39,39,39,39,128,39,39,]),'NOUM':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'GEMEO':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'NAOGEMEO':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'MAISPIQUENO':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'MAISPIQUENOOUGEMEO':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'MAISGRANDE':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'MAISGRANDEOUGEMEO':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'COM':([26,27,28,47,48,49,50,99,138,],[51,52,54,51,54,51,54,113,142,]),'ABREPR':([27,31,54,99,102,113,],[53,57,80,112,116,80,]),'SOMA':([34,35,36,37,38,39,58,59,60,61,76,77,78,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,119,120,121,122,123,124,125,126,129,132,133,134,135,136,137,146,],[-47,62,-11,-12,-45,-46,-12,62,-47,-12,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-33,62,62,62,62,62,62,62,62,62,-34,-35,-36,-37,-38,-39,62,]),'MENUS':([34,35,36,37,38,39,58,59,60,61,76,77,78,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,119,120,121,122,123,124,125,126,129,132,133,134,135,136,137,146,],[-47,63,-11,-12,-45,-46,-12,63,-47,-12,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-33,63,63,63,63,63,63,63,63,63,-34,-35,-36,-37,-38,-39,63,]),'SOMANBEZES':([34,35,36,37,38,39,58,59,60,61,76,77,78,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,119,120,121,122,123,124,125,126,129,132,133,134,135,136,137,146,],[-47,64,-11,-12,-45,-46,-12,64,-47,-12,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-33,64,64,64,64,64,64,64,64,64,-34,-35,-36,-37,-38,-39,64,]),'DIBIDE':([34,35,36,37,38,39,58,59,60,61,76,77,78,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,119,120,121,122,123,124,125,126,129,132,133,134,135,136,137,146,],[-47,65,-11,-12,-45,-46,-12,65,-47,-12,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-33,65,65,65,65,65,65,65,65,65,-34,-35,-36,-37,-38,-39,65,]),'SOBRAS':([34,35,36,37,38,39,58,59,60,61,76,77,78,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,119,120,121,122,123,124,125,126,129,132,133,134,135,136,137,146,],[-47,66,-11,-12,-45,-46,-12,66,-47,-12,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,-33,66,66,66,66,66,66,66,66,66,-34,-35,-36,-37,-38,-39,66,]),'IE':([34,35,36,37,38,39,58,59,60,61,76,77,78,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,119,120,121,122,123,124,125,126,129,132,133,134,135,136,137,146,],[-47,67,-11,-12,-45,-46,-12,67,-47,-12,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-33,67,67,67,67,67,67,67,67,67,-34,-35,-36,-37,-38,-39,67,]),'OUE':([34,35,36,37,38,39,58,59,60,61,76,77,78,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,119,120,121,122,123,124,125,126,129,132,133,134,135,136,137,146,],[-47,68,-11,-12,-45,-46,-12,68,-47,-12,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,-33,68,68,68,68,68,68,68,68,68,-34,-35,-36,-37,-38,-39,68,]),'FECHAPR':([36,37,38,39,60,78,82,85,86,87,88,89,90,91,100,101,105,125,128,129,132,133,134,135,136,137,],[-11,-12,-45,-46,-47,99,102,-28,-29,-30,-31,-32,-40,-41,114,-49,-33,138,-50,139,-34,-35,-36,-37,-38,-39,]),'FECHAPC':([36,37,38,39,58,60,61,85,86,87,88,89,90,91,92,105,119,120,121,122,123,124,132,133,134,135,136,137,],[-11,-12,-45,-46,83,-47,84,-28,-29,-30,-31,-32,-40,-41,105,-33,132,133,134,135,136,137,-34,-35,-36,-37,-38,-39,]),'VIRG':([36,37,38,39,60,85,86,87,88,89,90,91,93,94,95,96,97,98,100,101,105,128,132,133,134,135,136,137,],[-11,-12,-45,-46,-47,-28,-29,-30,-31,-32,-40,-41,106,107,108,109,110,111,115,-49,-33,-50,-34,-35,-36,-37,-38,-39,]),'ENTAO':([83,],[103,]),'FAZ':([84,],[104,]),'ABRECHAV':([103,104,143,],[117,118,147,]),'SENAO':([140,],[143,]),'FIM':([140,141,149,],[144,145,150,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'Decls':([0,],[2,]),'Atrib':([0,2,3,9,20,117,118,147,],[3,20,20,20,20,20,20,20,]),'Corpo':([0,2,3,9,20,117,118,147,],[4,18,23,29,23,130,131,148,]),'Decl':([0,2,],[5,19,]),'Proc':([0,2,3,9,20,117,118,147,],[9,9,9,9,9,9,9,9,]),'if':([0,2,3,9,20,117,118,147,],[11,11,11,11,11,11,11,11,]),'while':([0,2,3,9,20,117,118,147,],[12,12,12,12,12,12,12,12,]),'saidas':([0,2,3,9,20,117,118,147,],[13,13,13,13,13,13,13,13,]),'expr':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[35,59,59,76,77,78,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,119,120,121,122,123,124,125,126,129,146,]),'exprArit':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'exprRel':([17,32,33,51,52,53,57,62,63,64,65,66,67,68,69,70,71,72,73,74,75,106,107,108,109,110,111,112,113,116,142,],[37,58,61,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'lista':([54,113,],[79,127,]),'elems':([80,],[100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> Decls','Programa',1,'p_Programa_Empty','yacc3.py',13),
  ('Programa -> Atrib','Programa',1,'p_Programa_Empty','yacc3.py',14),
  ('Programa -> Decls Corpo','Programa',2,'p_Programa','yacc3.py',20),
  ('Programa -> Corpo','Programa',1,'p_Programa_Corpo','yacc3.py',26),
  ('Corpo -> Proc','Corpo',1,'p_Corpo','yacc3.py',32),
  ('Corpo -> Atrib','Corpo',1,'p_Corpo','yacc3.py',33),
  ('Corpo -> Proc Corpo','Corpo',2,'p_Corpo_Rec','yacc3.py',39),
  ('Corpo -> Atrib Corpo','Corpo',2,'p_Corpo_Rec','yacc3.py',40),
  ('Decls -> Decl','Decls',1,'p_Decls','yacc3.py',45),
  ('Decls -> Decls Decl','Decls',2,'p_DeclsRec','yacc3.py',49),
  ('expr -> exprArit','expr',1,'p_expr_arit','yacc3.py',55),
  ('expr -> exprRel','expr',1,'p_expr_arit','yacc3.py',56),
  ('Proc -> if','Proc',1,'p_Proc','yacc3.py',63),
  ('Proc -> while','Proc',1,'p_Proc','yacc3.py',64),
  ('Proc -> saidas','Proc',1,'p_Proc','yacc3.py',65),
  ('Decl -> VAR ID','Decl',2,'p_Decl','yacc3.py',72),
  ('Atrib -> VAR ID COM expr','Atrib',4,'p_Atrib_expr','yacc3.py',85),
  ('Atrib -> ALTERNA ID COM expr','Atrib',4,'p_alterna_var','yacc3.py',99),
  ('Decl -> LISTA ID','Decl',2,'p_Decl_Lista_NoSize','yacc3.py',108),
  ('Decl -> LISTA ID INT','Decl',3,'p_DeclLista_Size','yacc3.py',122),
  ('Atrib -> ALTERNA ID ABREPR expr FECHAPR ABREPR expr FECHAPR COM expr','Atrib',10,'p_AtribMatriz_comExpr','yacc3.py',139),
  ('Atrib -> ALTERNA ID ABREPR expr FECHAPR COM lista','Atrib',7,'p_AtribMatriz_comLista','yacc3.py',154),
  ('Atrib -> ALTERNA ID ABREPR expr FECHAPR COM expr','Atrib',7,'p_AlternaLista_elem','yacc3.py',180),
  ('Atrib -> LISTA ID COM lista','Atrib',4,'p_AtribLista_lista','yacc3.py',197),
  ('Decl -> MATRIZ ID','Decl',2,'p_Decl_Matriz_NoSize','yacc3.py',215),
  ('Decl -> MATRIZ ID INT INT','Decl',4,'p_DeclMatriz_Size','yacc3.py',229),
  ('Proc -> BUSCA ID ABREPR expr FECHAPR','Proc',5,'p_ProcBusca_Lista','yacc3.py',243),
  ('exprArit -> expr SOMA expr','exprArit',3,'p_soma','yacc3.py',255),
  ('exprArit -> expr MENUS expr','exprArit',3,'p_sub','yacc3.py',259),
  ('exprArit -> expr SOMANBEZES expr','exprArit',3,'p_mult','yacc3.py',263),
  ('exprArit -> expr DIBIDE expr','exprArit',3,'p_div','yacc3.py',267),
  ('exprArit -> expr SOBRAS expr','exprArit',3,'p_rem','yacc3.py',271),
  ('exprRel -> NOUM ABREPC expr FECHAPC','exprRel',4,'p_not','yacc3.py',275),
  ('exprRel -> GEMEO ABREPC expr VIRG expr FECHAPC','exprRel',6,'p_gemeo','yacc3.py',279),
  ('exprRel -> NAOGEMEO ABREPC expr VIRG expr FECHAPC','exprRel',6,'p_naogemeo','yacc3.py',283),
  ('exprRel -> MAISPIQUENO ABREPC expr VIRG expr FECHAPC','exprRel',6,'p_inf','yacc3.py',287),
  ('exprRel -> MAISPIQUENOOUGEMEO ABREPC expr VIRG expr FECHAPC','exprRel',6,'p_infeq','yacc3.py',291),
  ('exprRel -> MAISGRANDE ABREPC expr VIRG expr FECHAPC','exprRel',6,'p_sup','yacc3.py',295),
  ('exprRel -> MAISGRANDEOUGEMEO ABREPC expr VIRG expr FECHAPC','exprRel',6,'p_supeq','yacc3.py',299),
  ('exprRel -> expr IE expr','exprRel',3,'p_ie','yacc3.py',303),
  ('exprRel -> expr OUE expr','exprRel',3,'p_oue','yacc3.py',307),
  ('if -> SE ABREPC exprRel FECHAPC ENTAO ABRECHAV Corpo FECHACHAV SENAO ABRECHAV Corpo FECHACHAV FIM','if',13,'p_if_Then_Else','yacc3.py',312),
  ('if -> SE ABREPC exprRel FECHAPC ENTAO ABRECHAV Corpo FECHACHAV FIM','if',9,'p_if_Then','yacc3.py',317),
  ('while -> ENQUANTO ABREPC exprRel FECHAPC FAZ ABRECHAV Corpo FECHACHAV FIM','while',9,'p_while','yacc3.py',322),
  ('expr -> ENTRADAS','expr',1,'p_expr_in','yacc3.py',329),
  ('expr -> INT','expr',1,'p_expr','yacc3.py',333),
  ('expr -> ID','expr',1,'p_expr_var','yacc3.py',337),
  ('lista -> ABREPR elems FECHAPR','lista',3,'p_lista','yacc3.py',345),
  ('elems -> INT','elems',1,'p_elems','yacc3.py',349),
  ('elems -> elems VIRG INT','elems',3,'p_elems_rec','yacc3.py',353),
  ('Proc -> BUSCA ID ABREPR expr FECHAPR ABREPR expr FECHAPR','Proc',8,'p_ProcBusca_Matriz','yacc3.py',358),
  ('saidas -> SAIDAS ID','saidas',2,'p_saidas_STRING','yacc3.py',371),
  ('saidas -> SAIDAS expr','saidas',2,'p_saidas_OP','yacc3.py',375),
]
