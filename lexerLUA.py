# lexer.py


# buscar difrernecia entre sly y ply 

import sly

class Lexer(sly.Lexer):
	# Se debe definir tokens

	
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
		NIL, 
		NOT, 
		OR,
		REPEAT, 
		RETURN, 
		THEN, 
		TRUE, 
		UNTIL, 
		WHILE,
		

		# Operadores de relacion ((( que es eso ?)))
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


	# consutlar diferencia o conistencia de los literals en SLY ------------------------------ strings 

	literals = "+-*/%^#=(){}[];:,."


	# Espacios en blanco
	ignore = " \t"


	
	@_(r'\n+')
	def ignore_newline(self, t):
		self.lineno += len(t.value)
	
	# Expresiones regulares para tokens

	STRING = r'".*"'
	
	# Operadores   ( WTF ?! )
	EQ = r"=="
	NE = r"~="
	LE = r"<="
	GE = r">="
	LT = r"<"
	GT = r">"

	# Identificadores ((( esto es igual que el define en PLY ?)))

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
	ID["nil"] = NIL      # revisar para que sirve
	ID["not"] = NOT
	ID["or"] = OR
	ID["repeat"] = REPEAT
	ID["return"] = RETURN
	ID["then"] = THEN
	ID["true"] = TRUE
	ID["until"] = UNTIL
	ID["while"] = WHILE






	#Reconocimiento de enteros y hexadecimales ( para el hexadecimal se antepone 0x para identificarlo)

	@_(r'\d+', r'0x[0-9a-fA-F]+') #esto reconoce los hexadecimales
	def NUMBER(self, t):
		if t.value.startswith('0x'):  # deben iniciar com 0x
			t.value = int(t.value[2:], 16)
		else:
			t.value = int(t.value)
		return t



	# Error handling rule
	def error(self, t):
		print('Linea %d: Caracter ilegal %r' % (self.lineno, t.value[0]))
		self.index += 1
		


		# aja ... es la prueba ?? 
		
if __name__ == '__main__':
    lua = '''do
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
    for tok in lexer.tokenize(lua):
        print(tok)