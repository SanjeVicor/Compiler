import argparse
import lexicalAnalyzerv1 as lexicalAnalyzer
import syntactic
import semantic
import time
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
parser.add_argument("-f", "--file", help="Nombre de archivo a procesar")
args = parser.parse_args()
 
fileName = args.file

instructionList , errorList = lexicalAnalyzer.main(fileName)


if errorList:
    for e in errorList:
        print(f"[-] Error : {e}")
else:
       
    for e in instructionList:
        for inst in e:
            print(f"[+] Success : {inst.getInstruction()} --> {inst.getMessage()} ---> {inst.getLine()} \n") 
        
    lineList , errorList= syntactic.main(fileName)
    print('-----------------------------------------------')
    
    
    
    if errorList:
        errorList.sort(key=lambda x:x.getNline())
        for e in errorList:
            print(f"[-] Error : {e.getInstruction()}, linea {e.getNline()} \n")
    elif lineList:
        for inst in lineList:
            print(f"[+] Success : {inst.getInstruction()}, linea {inst.getNline()}, tipo {inst.getType()} \n") 
        
        print('-----------------------------------------------')
        semantic.main(instructionList, lineList)
