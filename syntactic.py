import re
from InstructionLine import InstructionLine


#Llamadas a funciones --> ERROR :
"""
1)
__asm__ __volatile__("movl %1, %%eax;"
    "movl %2, %%ebx;"
    "addl %%ebx, %%eax;"
  "movl %%eax, %0;" : "=g" ( $result ) : "g" ( $a ), "g" ( $b ));


"""
#Solucion : Buscar parentesis como en funciones con las llaves 


instructionRegexList = list()

instructionRegexList.append({'expression' : r"return\s+(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*|true|false)\s*;", 'type' : 'return'})
instructionRegexList.append({'expression' : r"#include.*", 'type' : 'library'})
instructionRegexList.append({'expression' : r"\s*(int|char|string|void|float|double|bool)\s+(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*\x28(\s*(int|char|string|void|float|double)\s+(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)+(\s*,\s*((int|char|string|void|float|double|bool)\s+(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*)*\x29\s*(\x7b)?" , 'type' : 'function-parameters'})
instructionRegexList.append({'expression' : r"\s*(int|char|string|void|float|double|bool)\s+(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*\x28\s*\x29\s*(\x7b)?", 'type' : 'function'})
#instructionRegexList.append({'expression' : r"\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*\x28(\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*|true|false|\d+(\d+(\x2e)\d{1,16})?))(\s*,\s*(\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*|true|false|\d+(\d+(\x2e)\d{1,16})?)))*\x29;", 'type' : 'call'})
instructionRegexList.append({'expression' : r"((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*(\x5f)*\s+)?\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*(\x5f)*\s*\x28.*\x29;", 'type' : 'call'})
instructionRegexList.append({'expression' : r"if\x28\s*((\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*))\s*\x29\s*(({?)\s*(}?))?", 'type' : 'if'})
instructionRegexList.append({'expression' : r"else\s+if\x28\s*((\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*))\s*\x29(\s*({?)\s*(}?))?", 'type' : 'elsf'})
instructionRegexList.append({'expression' : r"else\s*({?)\s*(}?)", 'type' : 'else'})
instructionRegexList.append({'expression' : r"for\s*\x28\s*(int|float|long)?\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*((=)\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*|\d+))?\s*(;)\s*(((\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)))?\s*(;)\s*(((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*|\d+)+(--|\+\+))?\s*\x29\s*({?)\s*(}?)", 'type' : 'for'})
instructionRegexList.append({'expression' : r"while\x28\s*((\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*|(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*))\s*\x29\s*({?)\s*(}?)", 'type' : 'while'})
instructionRegexList.append({'expression' : r"do({)?", 'type' : 'do'})
instructionRegexList.append({'expression' : r"(})?while\x28\s*((\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*))\s*\x29\s*;", 'type' : 'do-while'})

instructionRegexList.append({'expression' : r"\s*\x7b", 'type' : '{'})
instructionRegexList.append({'expression' : r"\s*\x7d", 'type' : '}'})

instructionRegexList.append({'expression' : r"//.*", 'type' : 'comentario'})


#declaracion de variables
instructionRegexList.append({'expression' : r"\s*(int\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+)?(\s*,\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+)?)*\s*;", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(double\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?))*\s*;", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(float\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?))*\s*;", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(string\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)))?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)))?))*\s*;", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(char\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x27.?\x27)))?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x27.?\x27)))))*\s*;", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(bool\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?(\s*,\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?)*\s*;", 'type' : 'variable_instance'})

instructionRegexList.append({'expression' : r"\s*(int\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+)?(\s*,\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+)?)*\s*;", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(float\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?))*\s*;", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(double\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?))*\s*;", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(string\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)))?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)))?))*\s*;", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(char\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x27.?\x27)))?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x27.?\x27)))))*\s*", 'type' : 'variable_instance'})
instructionRegexList.append({'expression' : r"\s*(bool\s+)(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?(\s*,\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?)*\s*;", 'type' : 'variable_instance'})

instructionRegexList.append({'expression' : r"((int|float|double)\s+)((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(=|\x2a=|\x2b=|\x2d=|\x2f=)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)(\s*((\x2a|\x2b|\x2d|\x2f)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*))*;", 'type' : 'variable_instance_operation'})
instructionRegexList.append({'expression' : r"((int|float|double)\s+)((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(\x2a{2}|\x2b{2}|\x2d{2})\s*;", 'type' : 'variable_instance_operation'})

#arreglos 
instructionRegexList.append({'expression' : r"\s*int\s+(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\x5b((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*|\d)\x5d\s*(=\s*\d)?;", 'type' : 'array'})


#igualacion de variables
instructionRegexList.append({'expression' : r"\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+)?(\s*,\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+)?)*\s*;", 'type' : 'variable'})
instructionRegexList.append({'expression' : r"\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?))*\s*;", 'type' : 'variable'})
instructionRegexList.append({'expression' : r"\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?))*\s*;", 'type' : 'variable'})
instructionRegexList.append({'expression' : r"\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)))?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)))?))*\s*;", 'type' : 'variable'})
instructionRegexList.append({'expression' : r"\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x27.?\x27)))?(\s*,\s*((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*((\x27.?\x27)))))*\s*", 'type' : 'variable'})
instructionRegexList.append({'expression' : r"\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?(\s*,\s*(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?)*\s*;", 'type' : 'variable'})

#operaciones
instructionRegexList.append({'expression' : r"((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(=|\x2a=|\x2b=|\x2d=|\x2f=)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)(\s*((\x2a|\x2b|\x2d|\x2f)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*))*;", 'type' : 'number_operation'})
#instructionRegexList.append(r"((int|float|double)\s+)?((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(\x2a=|\x2b=|\x2d=|\x2f=)\s*(\d+|(\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*;")
instructionRegexList.append({'expression' : r"((\x5f|\x24|\x2a)*[a-zA-Z](\w|\d)*)\s*(\x2a{2}|\x2b{2}|\x2d{2})\s*;", 'type' : 'number_operation'})




def main(fileName):
    global instructionRegexList
    instructionSuccess = list()
    instructionErrorList = list()
    
    with open(fileName) as file:
        i = 0
        for line in file:
            i += 1 
            found = False
            if line != '\n':
                for key in instructionRegexList: 
                    if len(line) == 0:
                        break 
                    line = line.strip()
                    match = re.fullmatch(key["expression"], line) 
                    if match:
                        found = True
                        instruction = line[match.start():match.end()]
                        line = re.sub(key["expression"],' ',line)
                        instructionObj = InstructionLine(instruction,i,key["type"])
                        instructionSuccess.append(instructionObj)     
                if not found and line != "" : 
                    instructionObj = InstructionLine(line,i, 'None')
                    instructionErrorList.append(instructionObj)
    file.close()
    
    if instructionSuccess:
        x = 0
        y = 0
        i = 0
        errorBracket = False
        for instruction in instructionSuccess:
            BracketOpen = re.search('{',instruction.getInstruction())
            BracketClose = re.search('}',instruction.getInstruction())
            if BracketOpen:
                x += 1
                lastOpenPos = instruction
                
            elif BracketClose:
                y += 1
                lastClosePos = instruction
            

        if x > y: 
            instructionErrorList.append(lastOpenPos)
            return instructionSuccess, instructionErrorList 
        elif x < y:
            instructionErrorList.append(lastClosePos)
            return instructionSuccess, instructionErrorList 
        
        return instructionSuccess, instructionErrorList 

