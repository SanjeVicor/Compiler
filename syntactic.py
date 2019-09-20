import re
from InstructionLine import InstructionLine

instructionRegexList = list()

instructionRegexList.append(r"return\s+(\d+|(\x5f)?[a-zA-Z](\w|\d)*|true|false)\s*;")

instructionRegexList.append(r"\s*(int|char|string|void|float|double|bool)\s+(\x5f)?[a-zA-Z](\w|\d)*\s*\x28((int|char|string|void|float|double)\s+(\x5f)?[a-zA-Z](\w|\d)*)*(\s*,\s*((int|char|string|void|float|double|bool)\s+(\x5f)?[a-zA-Z](\w|\d)*))*\x29\s*(\x7b)?")
instructionRegexList.append(r"if\x28\s*((\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*))\s*\x29\s*(({?)\s*(}?))?")
instructionRegexList.append(r"elif\x28\s*((\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*))\s*\x29(\s*({?)\s*(}?))?")
instructionRegexList.append(r"else\s*({?)\s*(}?)")
instructionRegexList.append(r"for\s*\x28\s*(int|float|long)?\s*(\w+|\d+)\s*((=)\s*(\w+|\d+))?\s*(;)\s*(((\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*)))?\s*(;)\s*((\w+|\d+)+(--|\+\+))?\s*\x29\s*({?)\s*(}?)")
instructionRegexList.append(r"while\x28\s*((\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*))\s*\x29\s*({?)\s*(}?)")
instructionRegexList.append(r"do({)?")
instructionRegexList.append(r"(})?while\x28\s*((\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*))\s*\x29\s*;")

instructionRegexList.append(r"\s*\x7b")
instructionRegexList.append(r"\s*\x7d")

instructionRegexList.append(r"//.*")

#operaciones
instructionRegexList.append(r"((int|float|double)\s+)?((\x5f)?[a-zA-Z](\w|\d)*)\s*=\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*((\x2a|\x2b|\x2d|\x2f)\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*)?;")
instructionRegexList.append(r"((int|float|double)\s+)?((\x5f)?[a-zA-Z](\w|\d)*)\s*(\x2a=|\x2b=|\x2d=|\x2f=)\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*;")
instructionRegexList.append(r"((int|float|double)\s+)?((\x5f)?[a-zA-Z](\w|\d)*)\s*(\x2a{2}|\x2b{2}|\x2d{2})\s*;")

#igualacion de variables
instructionRegexList.append(r"\s*(int\s+)?(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+)?(\s*,\s*(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+)?)*\s*;")
instructionRegexList.append(r"\s*(float\s+)?(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?))*\s*;")
instructionRegexList.append(r"\s*(double\s+)?(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?))*\s*;")
instructionRegexList.append(r"\s*(string\s+)?(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)|(\x27.*\x27)))?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)|(\x27.*\x27)))?))*\s*;")
instructionRegexList.append(r"\s*(char\s+)?(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.?\x22)|(\x27.?\x27)))?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.?\x22)|(\x27.?\x27)))))*\s*")
instructionRegexList.append(r"\s*(bool\s+)?(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?(\s*,\s*(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?)*\s*;")


#declaracion de variables
instructionRegexList.append(r"\s*(int\s+)(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+)?(\s*,\s*(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+)?)*\s*;")
instructionRegexList.append(r"\s*(float\s+)(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,7})?)?))*\s*;")
instructionRegexList.append(r"\s*(double\s+)(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+((\x2e)\d{1,16})?)?))*\s*;")
instructionRegexList.append(r"\s*(string\s+)(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)|(\x27.*\x27)))?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)|(\x27.*\x27)))?))*\s*;")
instructionRegexList.append(r"\s*(char\s+)(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.?\x22)|(\x27.?\x27)))?(\s*,\s*((\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.?\x22)|(\x27.?\x27)))))*\s*")
instructionRegexList.append(r"\s*(bool\s+)(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?(\s*,\s*(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?)*\s*;")

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
                    line = line.strip()
                    match = re.match(key, line)
                    #print(match)
                    if match:
                        #print(f"{match} , {key}")
                        #print(f"{line} , {match}")
                        found = True
                        instruction = line[match.start():match.end()]
                        line = re.sub(key,' ',line)
                        #print(f"{line} , {instruction} , {key}")
                        instructionObj = InstructionLine(instruction)
                        instructionSuccess.append(instructionObj)     
                if not found :
                       instructionErrorList.append(line)
      file.close()
      
      if instructionSuccess:
          x = 0
          y = 0
          for instruction in instructionSuccess:
              print(instruction)
              BracketOpen = re.search('{',instruction.getInstruction())
              BracketClose = re.search('}',instruction.getInstruction())
              if BracketOpen:
                  x += 1
              elif BracketClose:
                  y += 1

          if x != y:
              errorBracket = True
          else:
              errorBracket = False
            
      return instructionSuccess, instructionErrorList , errorBracket

