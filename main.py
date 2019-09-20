import argparse
import lexicalAnalyzerv1 as lexicalAnalyzer
import syntactic

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
    for inst in instructionList:
        print(f"[+] Success : {inst.getInstruction()} --> {inst.getMessage()} \n") 
    instructionList , errorList, errorBrackets = syntactic.main(fileName)
    print('-----------------------------------------------')
    if errorList:
        for e in errorList:
            print(f"[-] Error : {e} \n")
    if instructionList:
        for inst in instructionList:
            print(f"[+] Success : {inst.getInstruction()} \n") 
    if errorBrackets:
        print("[!] ERROR en los cierres de llaves")