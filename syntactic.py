import re
from InstructionLine import InstructionLine

instructionRegexList = list()

instructionRegexList.append(r"\s*int\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+)?(\s*,\s*(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+)?)*\s*;")
instructionRegexList.append(r"\s*float\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?))*\s*;")
instructionRegexList.append(r"\s*double\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?))*\s*;")
instructionRegexList.append(r"\s*string\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)|(\x27.*\x27)))?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)|(\x27.*\x27)))?))*\s*;")
instructionRegexList.append(r"\s*char\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.?\x22)|(\x27.?\x27)))?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.?\x22)|(\x27.?\x27)))))*\s*")
instructionRegexList.append(r"\s*bool\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?(\s*,\s*(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?)*\s*;")
instructionRegexList.append(r"\s*\x7b")
instructionRegexList.append(r"\s*\x7d")
instructionRegexList.append(r"\s*(int|char|string|void|float|double|bool)\s+(\x5f)?[a-zA-Z](\w|\d)*\s*\x28((int|char|string|void|float|double)\s+(\x5f)?[a-zA-Z](\w|\d)*)*(\s*,\s*((int|char|string|void|float|double|bool)\s+(\x5f)?[a-zA-Z](\w|\d)*))*\x29\s*(\x7b)?")
#instructionRegexList.append(r"")

def main(fileName):
      global instructionRegexList
      instructionSuccess = list()
      instructionErrorList = list()
      
      with open(fileName) as file:
         
        for line in file: 
            found = False
            if line != '\n':
                for key in instructionRegexList: 
                    if len(line) == 0:
                        break
                    match = re.match(key, line)
                    line = line.strip()
                    if match:
                        #print(f"{line} , {match}")
                        found = True
                        instruction = line[match.start():match.end()]
                        line = re.sub(key,' ',line)
                        instructionObj = InstructionLine(instruction)
                        instructionSuccess.append(instructionObj)     
                if not found :
                       instructionErrorList.append(line)
      file.close()
      return instructionSuccess, instructionErrorList 


"""
def main(fileName):
   Utilizar la tecnica del lexico debido a los siguientes escenarios
    
   1) int x=10; char s = 'z'; ERROR
   
   2) int x = 10 , s = 20;
   
   3) int x=10;
      char s = 'z';
      
    return listaDeInstruction o error
"""