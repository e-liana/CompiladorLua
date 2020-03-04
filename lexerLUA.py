#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Analizador Lexico para LUA 5.1
# Eliana Osorio R.

import sly

class Lexer(sly.Lexer):



	tokens = {

		# Palabras Reservadas

		AND,
		BREAK, 
		DO, 
		ELSE, 
		ELSEIF,
		END, 
		FALSE, 
		FOR, 
		FUNCTION, 
		IF,
		IN, 
		LOCAL, 
		NIL,  # Nil es el tipo del valor nil, cuya principal propiedad es ser diferente de cualquier otro valor
		NOT, 
		OR,
		REPEAT, 
		RETURN, 
		THEN, 
		TRUE, 
		UNTIL, 
		WHILE,
		

		# Operadores de relacion 
		EQ, 
		NE, 
		LE, 
		GE, 
		LT, 
		GT,
		
		# Identificador
		ID,
		
		# Constante
		NUMBER, 
		STRING,

	}


	#A literal character is a single character that is returned “as is” when encountered by the lexer.

	literals = "+-*/%^#=(){}[];:,."


	# Espacios en blanco
	ignore = " \t"


	# Define a rule so we can track line numbers
	@_(r'\n+')
	def ignore_newline(self, t):
		self.lineno += len(t.value)
	
	# Expresiones regulares para tokens

	STRING = r'".*"'
	
	# Operadores  
	EQ = r"=="
	NE = r"~="
	LE = r"<="
	GE = r">="
	LT = r"<"
	GT = r">"

	# Identificadores ( reconocer tokens en minuscula y mayuscula)

	ID = r"[a-zA-Z_][a-zA-Z0-9_]*"
	ID["and"] = AND
	ID["break"] = BREAK
	ID["do"] = DO
	ID["else"] = ELSE
	ID["elseif"] = ELSEIF
	ID["end"] = END
	ID["false"] = FALSE
	ID["for"] = FOR
	ID["function"] = FUNCTION
	ID["if"] = IF
	ID["in"] = IN
	ID["local"] = LOCAL
	ID["nil"] = NIL     
	ID["not"] = NOT
	ID["or"] = OR
	ID["repeat"] = REPEAT
	ID["return"] = RETURN
	ID["then"] = THEN
	ID["true"] = TRUE
	ID["until"] = UNTIL
	ID["while"] = WHILE




	# Lua acepta constantes enteras hexadecimales, escritas anteponiendo el prefijo 0x.

	@_(r'\d+', r'0x[0-9a-fA-F]+')
	def NUMBER(self, t):
		if t.value.startswith('0x'):
			t.value = int(t.value[2:], 16)
		else:
			t.value = int(t.value)
		return t



	# Error handling rule
	def error(self, t):
		print('Linea %d: Caracter ilegal %r' % (self.lineno, t.value[0]))
		self.index += 1
		


	# Prueba	
		
if __name__ == '__main__':
    PruebaLua = '''do
       local var, limit, step = tonumber(e1), tonumber(e2), tonumber(e3)
       if not (var and limit and step) then error() end
       while (step > 0 and var <= limit) or (step <= 0 and var >= limit) do
         local v = var
         block
         var = var + step
       end
     end
	'''
	
    lexer = Lexer()
    for tok in lexer.tokenize(PruebaLua):
        print(tok)
