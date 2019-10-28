import re
variableList = dict()
operationList = list()

#Valores disponibles/validos para las variables
stringList =dict()
charList = dict()
numberList = dict()
boolList = dict()

def getLexicalInstuctionList(instructionNline, lexicalList):
    for e in lexicalList:
        for inst in e:
            if instructionNline == inst.getLine():
                #print(f"{e} -- > {instructionNline}")
                return e

def searchVariable(var, block):
    global variableList

    for k, v in variableList.items():
        if var == k:
            #print(f"search {var}, {k}")
            #print(f"search {block}")
            #print(v["block"])
            if block == v["block"]:
                return True
    return False

def getVariables(lexicalList,sintacticList):
    global stringList
    global charList
    global numberList
    global boolList
    global variableList
    
    number = False
    string = False
    char = False
    boolean = False
    block = 0
    for instS in sintacticList:
        if re.match(r"function", instS.getType()) :
            block +=1
        if re.match(r"variable_instance", instS.getType()) or re.fullmatch("function-parameters", instS.getType()):
            setList = getLexicalInstuctionList(instS.getNline(),lexicalList)
            for inst in setList:
                #print(inst.getInstruction())
                if inst.getMessage() == "Tipo de dato":
                    #print(inst.getInstruction())
                    if re.fullmatch(r"(int|float|double)",inst.getInstruction()):
                        number = True
                    elif inst.getInstruction() == "string":
                        string = True
                    elif inst.getInstruction() == "char":
                        char = True
                    elif inst.getInstruction() == "bool":
                        boolean= True
                elif inst.getMessage() == "identificador":
                    var = inst.getInstruction()
                    print(inst.getInstruction())
                    if searchVariable(var,block):
                    #if var in variableList:
                        print("Error")
                        print(f"variable {var} previamente declarada, linea {instS.getNline()}, bloque {block}")
                        print(variableList)
                        break
                    if number:
                        if var not in variableList: #Correcto
                            variableList[var] = {"variable" : "number", "line" : instS.getNline(), "block" :[] }
                        variableList[var]["block"].append(block)

                        #print(variableList[var])
                        #Todas son validas,menos string, revisar semantico_apuntes.txt
                        numberList[var] = {"variable" : "number", "line" : instS.getNline(),"block" :block }
                        boolList[var] = {"variable" : "number", "line" : instS.getNline(),"block" :block }
                        charList[var] = {"variable" : "number", "line" : instS.getNline(),"block" :block }
                        number = False
                    elif boolean:
                        if var not in variableList: #Correcto
                            variableList[var] = {"variable" : "bool", "line" : instS.getNline(), "block" :[] }
                        variableList[var]["block"].append(block)
                        numberList[var] = {"variable" : "bool", "line" : instS.getNline(),"block" :block }
                        boolList[var] = {"variable" : "bool", "line" : instS.getNline(),"block" :block }
                        charList[var] = {"variable" : "bool", "line" : instS.getNline(),"block" :block }
                        boolean = False
                    elif char:
                        #variableList[var] = "char"
                        if var not in variableList: #Correcto
                            variableList[var] = {"variable" : "char", "line" : instS.getNline(), "block" :[] }
                        variableList[var]["block"].append(block)
                        numberList[var] = {"variable" : "char", "line" : instS.getNline(),"block" :block }
                        boolList[var] = {"variable" : "char", "line" : instS.getNline(),"block" :block } #bool x = true; char y = 'd' + x ; Es valido
                        charList[var] = {"variable" : "char", "line" : instS.getNline(),"block" :block }
                        char = False
                    elif string:
                        #variableList[var] = "string"
                        if var not in variableList: #Correcto
                            variableList[var] = {"variable" : "string", "line" : instS.getNline(), "block" :[] }
                        variableList[var]["block"].append(block)
                        stringList[var] = {"variable" : "string", "line" : instS.getNline(),"block" :block }
                        string = False
                    #break
                # Obtener tipo de dato e identificador
                # Añadir a lista de variables y a su respectiva lista
                
                #print(f"[+] Success : {inst.getInstruction()} --> {inst.getMessage()} ---> {inst.getLine()} \n") 

def getFunctions(lexicalList,sintacticList):
    global variableList
    number = False
    string = False
    char = False
    boolean = False
    void = False
    for instS in sintacticList:
        if re.match(r"function", instS.getType()) :
            setList = getLexicalInstuctionList(instS.getNline(),lexicalList)
            for inst in setList:
                if inst.getMessage() == "Tipo de dato":
                   # print(inst.getInstruction())
                    if re.fullmatch(r"(int|float|double)",inst.getInstruction()):
                        number = True
                    elif inst.getInstruction() == "string":
                        string = True
                    elif inst.getInstruction() == "char":
                        char = True
                    elif inst.getInstruction() == "bool":
                        boolean= True
                    elif inst.getInstruction() == "void":
                        void= True
                elif inst.getMessage() == "identificador":
                    var = inst.getInstruction()
                    """
                    if var in variableList:
                        print("Error")
                        print(f"variable {var} previamente declarada, linea {instS.getNline()}")
                        print(variableList)
                        break
                    """
                    if number:
                        variableList[var] = {"type" : "function", "line" : instS.getNline()} 
                        number = False
                    elif boolean:
                        variableList[var] = {"type" : "function","line" : instS.getNline()} 
                        boolean = False
                    elif char:
                        #variableList[var] = "char"
                        variableList[var] = {"type" : "function","line" : instS.getNline()} 
                        char = False
                    elif string: 
                        variableList[var] = {"type" : "function","line" : instS.getNline()} 
                        string = False
                    elif void: 
                        variableList[var] = {"type" : "function", "line" : instS.getNline()} 
                        string = False
                    break

def getOperandos(instruction):
    print('\n')
    #opList = re.compile(r"(\x2a|\x2b|-|/|%|and|or|not|&&|\x7c\x7c|=|;|int|char|string|int|float|double|bool)").split(instruction)
    opList = re.sub(r"(\x2a|\x2b|-|/|%|and|or|not|&&|\x7c\x7c|=|;|\x28|\x29|\x7b|\x7d|int|char|string|int|float|double|bool|void)"," ",instruction)
    opList = opList.split()
    print(f"{instruction}  -- > {opList}")
    return opList

def operandosValidos(operandos, nLine, block):
    global stringList
    global charList
    global numberList
    global boolList
    global variableList
    for e in operandos:
        for key in variableList:
            if re.fullmatch(key, e):
                line = variableList[key]['line']
                if line == None or line <= nLine:
                    if variableList[key]["variable"] == "number":
                        found = False
                        for x in operandos:
                            found = False
                            for y in numberList:
                                if re.fullmatch(y,x):
                                    if numberList[y]['line'] == None or variableList[y]['line'] <= nLine:
                                        if numberList[y]['line'] != None:
                                            try:
                                                for nBlock in variableList[y]['block']:
                                                    if nBlock == block:
                                                        found = True
                                                        break
                                            except : 
                                                pass
                                        else:
                                            found = True
                                            break
                                    if found :
                                        break
                        if not found:
                            return False    
                    elif variableList[key]["variable"] == "char":
                        found = False
                        for x in operandos:
                            found = False
                            for y in charList:
                                if re.fullmatch(y,x):
                                    if charList[y]['line'] == None or variableList[y]['line'] <= nLine:
                                        if charList[y]['line'] != None:
                                            for nBlock in variableList[y]['block']:
                                                if nBlock == block:
                                                    found = True
                                                    break
                                        else:
                                            found = True
                                            break
                                    if found :
                                        break
                        if not found:
                            return False  
                    elif variableList[key]["variable"] == "bool":
                        found = False
                        for x in operandos:
                            found = False
                            for y in boolList:
                                if re.fullmatch(y,x):
                                    if boolList[y]['line'] == None or variableList[y]['line'] <= nLine:
                                        if boolList[y]['line'] != None:
                                            for nBlock in variableList[y]['block']:
                                                if nBlock == block:
                                                    found = True
                                                    break
                                        else:
                                            found = True
                                            break
                                    if found :
                                        break
                        if not found:
                            return False  
                    elif variableList[key]["variable"] == "string":
                        found = False
                        for x in operandos:
                            found = False
                            for y in stringList:
                                if re.fullmatch(y,x):
                                    if stringList[y]['line'] == None or variableList[y]['line'] <= nLine:
                                        if stringList[y]['line'] != None:
                                            for nBlock in variableList[y]['block']:
                                                if nBlock == block:
                                                    found = True
                                                    break
                                        else:
                                            found = True
                                            break
                                    if found :
                                        break
                        if not found:
                            return False  
    return True
        
def getOperations(lexicalList,sintacticList):
    global stringList
    global charList
    global numberList
    global boolList
    global variableList
    #Modificar el semantico --> operacion = True | False
    #if operacion
        # split operqadores
        # int x = y + z  --->  [x,y,z]
        # Buscar en lista global "x", ver su tipo
        #Es int por lo tanto buscar en la lista "number", todas las variables y valores disponibles
    block = 0
    for instS in sintacticList:
        if re.search(r"function", instS.getType()) :
            block += 1
        if re.search(r"operation", instS.getType()):
            operandos = getOperandos(instS.getInstruction())
            msg = operandosValidos(operandos,instS.getNline(), block)
            if not msg :
                print(f"error no es posible ejecutar la siguiente operación {instS.getInstruction()} , linea {instS.getNline()}")
            else:
                print(instS.getInstruction())
                print("todo correcto")
    """
    for e in lexicalList:
        for inst in e:
            if re.match("identificador", inst.getMessage()):
                print(inst.getInstruction())

            if re.match("operador", inst.getMessage()):
                print(inst.getInstruction())
    """

def searchCalls():
    #Dividir por identificadores, true, false, digitos
    #el primer objeto es la funcion a llamar, entonces buscar en VariableList si existe.
    #Cuantos parametros recibe?
    #Son validos?
    pass

def main(lexicalList,sintacticList):
    global stringList
    global charList
    global numberList
    global boolList
    global variableList
    
    variableList["false"] = {"variable" : "bool", "line": None, 'block' : None}
    variableList["true"] = {"variable" : "bool", "line": None, 'block' : None}
    variableList[r"\d+"] = {"variable" : "number", "line": None, 'block' : None}
    variableList[r"\x27.*\x27"] = {"variable" : "string", "line": None, 'block' : None}
    variableList[r"\x22.*\x22"] = {"variable" : "char", "line": None, 'block' : None}

    #Valores validos --> CORREGIR
    boolList["false"] = {"variable" : "bool", "line": None, 'block' : None}
    boolList["true"] = {"variable" : "bool", "line": None, 'block' : None}
    numberList[r"\d+"] = {"variable" : "number", "line": None, 'block' : None}
    #charList.append(r"\x27.*\x27") 
    stringList[r"\x27.*\x27"] = {"variable" : "string", "line": None, 'block' : None}
    stringList[r"\x22.*\x22"] = {"variable" : "char", "line": None, 'block' : None}

    #IDS
    getVariables(lexicalList,sintacticList)
    getFunctions(lexicalList,sintacticList)
    searchCalls()
    #Buscar Operaciones -> ¿Son posibles ?
    #Buscar Comparaciones --> ¿Son compatibles?
    getOperations(lexicalList,sintacticList)
    print('\n')
    print('\n')
    print(f"String : {stringList}")
    print('\n')
    print(f"char : {charList}")
    print('\n')
    print(f"number : {numberList}")
    print('\n')
    print(f"bool : {boolList}")
    print('\n')
    print('\n')
    print(f"{variableList}")
    print('\n')
    print('\n')
    for e in variableList:
        print(e)
