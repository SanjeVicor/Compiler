import re

compilersWords = {}

compilersWords['if'] = {'message':'Estructura de control condicional', 'expression' : 'if(\s*)'}
compilersWords['else'] = {'message':'Estructura de control condicional', 'expression' : ''}
compilersWords['elif'] = {'message':'Estructura de control condicional', 'expression' : ''}
compilersWords['for'] = {'message':'Estructura de control repetitiva', 'expression' : ''}
compilersWords['while'] = {'message':'Estructura de control repetitiva', 'expression' : ''}
compilersWords['do'] = {'message':'Estructura de control repetitiva', 'expression' : ''}
#--------------------
compilersWords['int'] = {'message':'Tipo de dato', 'expression' : ''}
compilersWords['char'] = {'message':'Tipo de dato', 'expression' : ''}
compilersWords['string'] = {'message':'Tipo de dato', 'expression' : ''}
compilersWords['float'] = {'message':'Tipo de dato', 'expression' : ''}
compilersWords['double'] = {'message':'Tipo de dato', 'expression' : ''}
compilersWords['bool'] = {'message':'tipo de dato', 'expression': ''}
#--------------------
compilersWords['return'] = {'message':'palabra reservada', 'expression' : ''}
compilersWords['break'] = {'message':'palabra reservada', 'expression' : ''}
#--------------------
compilersWords[';'] = {'message':'palabra reservada', 'expression' : ''}
compilersWords['+'] = {'message':'operador para suma', 'expression' : ''}
compilersWords['-'] = {'message':'operador para resta', 'expression' : ''}
compilersWords['*'] = {'message':'operador para multiplicación', 'expression' : ''}

compilersWords['/'] = {'message':'operador para division', 'expression' : ''}
compilersWords['%'] = {'message':'operador para modulo', 'expression' : ''}
compilersWords['='] = {'message':'operador de igualacion', 'expression' : r'(=|==)'} # = es de igualacion, == es comparativo
#--------------------
compilersWords['<'] = {'message':'operador de comparacion', 'expression' : r'(<|=<)'}
compilersWords['>'] = {'message':'operador de comparacion', 'expression' : r'(>|>=)'}
compilersWords['=='] = {'message':'operador de comparacion', 'expression' : r'(=|==)'} # = es de igualacion, == es comparativo
compilersWords['!='] = {'message':'operador de comparacion', 'expression' : r'(!|!=)'} # ! es logico, != es comparativo
#--------------------
compilersWords['&&'] = {'message':'operador logico AND', 'expression' : ''}
compilersWords['||'] = {'message':'operador logico OR', 'expression' : ''}
compilersWords['!'] = {'message':'operador de logico NOT', 'expression' : r'(!|!=)'} # ! es logico, != es comparativo
compilersWords['and'] = {'message':'operador logico AND', 'expression' : ''}
compilersWords['or'] = {'message':'operador logico OR', 'expression' : ''}
compilersWords['not'] = {'message':'operador de logico NOT', 'expression' : r'(!|!=)'} # ! es logico, != es comparativo
#--------------------
compilersWords['('] = {'message':'operador parentesis de apertura', 'expression' : ''}
compilersWords[')'] = {'message':'operador parentesis de cierre', 'expression' : ''}
compilersWords['{'] = {'message':'operador llave de apertura', 'expression' : ''}
compilersWords['}'] = {'message':'operador llave de cierre', 'expression' : ''}
compilersWords['['] = {'message':'operador corchete de apertura', 'expression' : ''}
compilersWords[']'] = {'message':'operador corchete de cierre', 'expression' : ''}


compilersExpressions = {}

compilersExpressions['id'] = {'message':'identificador', 'expression' : r'(\x5f)?[a-zA-Z](\w|\d)*'}
compilersExpressions['digits'] = {'message':'digito de tipo int', 'expression' : r'\d+'}
compilersExpressions['float_digits'] = {'message':'digito de tipo float', 'expression' : r'\d+(\x2e)\d{1,7}'}
compilersExpressions['double_digits'] = {'message':'digito de tipo double', 'expression' : r'\d+(\x2e)\d{1,16}'}

compilersWords['true'] = {'message' : 'valor booleano verdadero', 'expression' : ''}
compilersWords['false'] = {'message' : 'valor booleano false', 'expression' : '' }



strInput = ""
strInput = input("Introduce la cadena a evaluar : ")

instructionList = strInput.split() 

for word in instructionList :
    print("Analizando la instrucción : ", word)

    if word in compilersWords : 
        message = compilersWords[word]['message']
        print(message)
    elif re.fullmatch(compilersExpressions['id']['expression'], word):
        message = compilersExpressions['id']['message']
        print(message)
    elif re.fullmatch(compilersExpressions['float_digits']['expression'], word):
        message = compilersExpressions['float_digits']['message']
        print(message)
    elif re.fullmatch(compilersExpressions['double_digits']['expression'], word):
        message = compilersExpressions['double_digits']['message']
        print(message)
    elif re.fullmatch(compilersExpressions['digits']['expression'], word):
        message = compilersExpressions['digits']['message']
        print(message)
    else :
        print("ERROR... instrucción no encontrada")


#regularExpression = r"(if|else|elif|={1}|={2})" ERRONEO
#print(re.findall(regularExpression,cadena))

''' IDEA PARA ANALIZADOR SINTACTICO
operadores = r"((\x2b)|-|(\x2d)|/)"
estructura_de_control_condicional = r"(if(\x52 .+ \x53)|else|elif)"
estructura_de_control_selectiva = r"switch"
estructura_de_control_repetitivas = r"(while|do|for)"
        
match = re.fullmatch(estructura_de_control_condicional, cadena)
if match:
    print(match)

'''
    
