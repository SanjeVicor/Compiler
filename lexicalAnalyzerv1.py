import re 
from Instruction import Instruction 

compilersWords = {}
compilersWords2 = {}

compilersWords[r'if'] = {'message':'Estructura de control condicional'}
compilersWords[r'else'] = {'message':'Estructura de control condicional'}
#compilersWords[r'elif'] = {'message':'Estructura de control condicional'}
compilersWords[r'for'] = {'message':'Estructura de control repetitiva'}
compilersWords[r'while'] = {'message':'Estructura de control repetitiva'}
compilersWords[r'do'] = {'message':'Estructura de control repetitiva'}
compilersWords[r'//.+'] = {'message':'Comentario', 'expression': '', 'type' : ''}
#--------------------
compilersWords[r'int\s+'] = {'message':'Tipo de dato'}
compilersWords[r'char\s+'] = {'message':'Tipo de dato'}
compilersWords[r'string\s+'] = {'message':'Tipo de dato'}
compilersWords[r'float\s+'] = {'message':'Tipo de dato'}
compilersWords[r'double\s+'] = {'message':'Tipo de dato'}
compilersWords[r'bool\s+'] = {'message':'tipo de dato', 'expression': '', 'type' : ''}
#--------------------
compilersWords[r'return'] = {'message':'palabra reservada'}
compilersWords[r'break'] = {'message':'palabra reservada'}
#--------------------
compilersWords[r','] = {'message':'coma'}
compilersWords[r'\x3B'] = {'message':'palabra reservada'}
compilersWords[r'\x2B'] = {'message':'operador para suma'}
compilersWords[r'-'] = {'message':'operador para resta'}
compilersWords[r'\x2A'] = {'message':'operador para multiplicación'}

compilersWords[r'\x22'] = {'message':'apertura/cierre de string'}
compilersWords[r'\x27'] = {'message':'apertura/cierre de char'}
compilersWords[r'/'] = {'message':'operador para division'}
compilersWords[r'%'] = {'message':'operador para modulo'}
compilersWords[r'='] = {'message':'operador de igualacion'} # = es de igualacion, == es comparativo
#--------------------
compilersWords[r'<'] = {'message':'operador de comparacion'}
compilersWords[r'>'] = {'message':'operador de comparacion'}
compilersWords[r'=='] = {'message':'operador de comparacion'} # = es de igualacion, == es comparativo
compilersWords[r'!='] = {'message':'operador de comparacion'} # ! es logico, != es comparativo
#--------------------
compilersWords[r'&&'] = {'message':'operador logico AND'}
compilersWords[r'\x7C\x7C'] = {'message':'operador logico OR'}
compilersWords[r'!'] = {'message':'operador de logico NOT'} # ! es logico, != es comparativo
compilersWords[r'and'] = {'message':'operador logico AND'}
compilersWords[r'or'] = {'message':'operador logico OR'}
compilersWords[r'not'] = {'message':'operador de logico NOT'} # ! es logico, != es comparativo
#--------------------
compilersWords[r'\x28'] = {'message':'operador parentesis de apertura'}
compilersWords[r'\x29'] = {'message':'operador parentesis de cierre'}
compilersWords[r'\x7B'] = {'message':'operador llave de apertura'}
compilersWords[r'\x7D'] = {'message':'operador llave de cierre'}
compilersWords[r'\x5B'] = {'message':'operador corchete de apertura'}
compilersWords[r'\x5D'] = {'message':'operador corchete de cierre'}


compilersWords[r'true'] = {'message' : 'valor booleano verdadero'}
compilersWords[r'false'] = {'message' : 'valor booleano false'}

compilersWords2[r'(\x5f)?[a-zA-Z](\w|\d)*'] = {'message':'identificador'}
compilersWords2[r'\d+'] = {'message':'digito de tipo int'}
compilersWords2[r'\d+(\x2e)\d{1,7}'] = {'message':'digito de tipo float'}
compilersWords2[r'\d+(\x2e)\d{1,16}'] = {'message':'digito de tipo double'}

def main(fileName): 
    global compilersWords
    global compilersWords2
    instructionSuccess = list()
    instructionErrorList = list()
    with open(fileName) as file:
        for line in file: 
            if line != '\n':
                for key in compilersWords: 
                    if len(line) == 0:
                        break
                    match = re.search(key, line)
                    if match:
                        instruction = line[match.start():match.end()]
                        line = re.sub(key,' ',line)
                        message = compilersWords[key]['message']
                        instructionObj = Instruction(instruction, message)
                        instructionSuccess.append(instructionObj)
                try:
                    x = line.split()
                    for element in x : 
                        found = False
                        for key in compilersWords2:
                            match = re.fullmatch(key,element)
                            if match: 
                                found = True
                                message = compilersWords2[key]['message'] 
                                instructionObj = Instruction(element, message)
                                instructionSuccess.append(instructionObj) 
                                break
                        if not found:
                            instructionErrorList.append(element)
                    
                except:
                    pass           
    file.close()
    return instructionSuccess, instructionErrorList                