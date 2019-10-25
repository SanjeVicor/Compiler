import re 
from Instruction import Instruction 
import time 
compilersWords = {}
compilersWords2 = {}

compilersWords[r'if'] = {'message':'Estructura de control condicional'}
compilersWords[r'else'] = {'message':'Estructura de control condicional'}
compilersWords[r'for'] = {'message':'Estructura de control repetitiva'}
compilersWords[r'while'] = {'message':'Estructura de control repetitiva'}
compilersWords[r'do'] = {'message':'Estructura de control repetitiva'}
compilersWords[r'//.+'] = {'message':'Comentario', 'expression': '', 'type' : ''}
#--------------------
compilersWords[r'int\s+'] = {'message':'Tipo de dato'}
compilersWords[r'void\s+'] = {'message':'Tipo de dato'}
compilersWords[r'char\s+'] = {'message':'Tipo de dato'}
compilersWords[r'string\s+'] = {'message':'Tipo de dato'}
compilersWords[r'float\s+'] = {'message':'Tipo de dato'}
compilersWords[r'double\s+'] = {'message':'Tipo de dato'}
compilersWords[r'bool\s+'] = {'message':'Tipo de dato', 'expression': '', 'type' : ''}
#--------------------
compilersWords[r'(\x5f)?[a-zA-Z](\w|\d)*'] = {'message':'identificador'}
#--------------------
compilersWords[r'return'] = {'message':'palabra reservada'}
compilersWords[r'break'] = {'message':'palabra reservada'}
#--------------------
compilersWords[r'='] = {'message':'operador de igualacion'} 

compilersWords[r'\x22.*\x22'] = {'message':'string'}
compilersWords[r'\x27.?\x27'] = {'message':'char'}
compilersWords[r'true'] = {'message' : 'valor booleano verdadero'}
compilersWords[r'false'] = {'message' : 'valor booleano false'}
compilersWords[r'\d+(\x2e)\d{1,7}'] = {'message':'digito de tipo float'}
compilersWords[r'\d+(\x2e)\d{1,16}'] = {'message':'digito de tipo double'}
compilersWords[r'\d+'] = {'message':'digito de tipo int'}


compilersWords[r','] = {'message':'coma'}
compilersWords[r'\x2B'] = {'message':'operador para suma'}
compilersWords[r'-'] = {'message':'operador para resta'}
compilersWords[r'\x2A'] = {'message':'operador para multiplicación'}


compilersWords[r'/'] = {'message':'operador para division'}
compilersWords[r'%'] = {'message':'operador para modulo'}
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
compilersWords[r'\x28'] = {'message':'parentesis de apertura'}
compilersWords[r'\x29'] = {'message':'parentesis de cierre'}
compilersWords[r'\x7B'] = {'message':'llave de apertura'}
compilersWords[r'\x7D'] = {'message':'llave de cierre'}
compilersWords[r'\x5B'] = {'message':'corchete de apertura'}
compilersWords[r'\x5D'] = {'message':'corchete de cierre'}



compilersWords[r'\x3B'] = {'message':'palabra reservada(punto y coma)'}

def main(fileName): 
    global compilersWords
    global compilersWords2
    instructionSuccess = list()
    instructionErrorList = list()
    i = 1
    with open(fileName) as file:
        for line in file: 
            instructionSuccessAux = list()
            if line != '\n':
                while len(line) > 0:
                    if re.fullmatch(r"\s+",line):
                        break
                    
                    #time.sleep(2)
                    for key in compilersWords: 
                        if len(line) == 0:
                            break
                        match = re.search(key, line)
                        if match:
                            #print(match)
                            #print(line)
                            instruction = line[match.start():match.end()]
                            #print(instruction)
                            line = line[0:match.start()] + line[match.end():] 
                            line = line.replace("\n", "")
                            instruction = instruction.replace(" ", "")
                            #print(line)
                            #print('-----------')
                            message = compilersWords[key]['message']
                            instructionObj = Instruction(instruction, message,i)
                            instructionSuccessAux.append(instructionObj)
                            
                instructionSuccess.append(instructionSuccessAux) 
            i += 1
    file.close()

    for i in range(len(instructionSuccess)):
        print(f"{i} --> {len(instructionSuccess[i])}")

    return instructionSuccess, instructionErrorList                