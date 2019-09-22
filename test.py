import re

#Decalarations
# int x;
# int x = 10;
intVar = r"int\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+)?\x3b"
floatVar = r"float\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*\d+(\x2e)\d{1,7})?\x3b"
doubleVar = r"double\s+(\x5f)?[a-zA-Z](\w|\d)*\s*=(\s*\d+(\x2e)\d{1,16})?\x3b"
charVar = r"char\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.?\x22)|(\x27.?\x27)))?\x3b"
stringVar = r"string\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*((\x22.*\x22)|(\x27.*\x27)))?\x3b"
boolVar = r"bool\s+(\x5f)?[a-zA-Z](\w|\d)*\s*(=\s*(true|false))?\x3b"
#Operations
numOp = r"(\x5f)?[a-zA-Z](\w|\d)*=((\x5f)?[a-zA-Z](\w|\d)*|\d+)(OPERATORS)((\x5f)?[a-zA-Z](\w|\d)*|\d+)"
strOp = r"((\x5f)?[a-zA-Z](\w|\d)*|\d+)=(((\x5f)?[a-zA-Z](\w|\d)*|\d+)|\w+)(OPERATORS)(((\x5f)?[a-zA-Z](\w|\d)*|\d+)|\w+)"
#Comparations
intCompar = r"(\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)"
floatCompar = r"(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)"

#if
ifRegExp = r"if\x28\s*((\d+|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,7}|(\x5f)?[a-zA-Z](\w|\d)*)|(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)\s*(<|>|<=|>=|!=|==)\s*(\d+(\x2e)\d{1,16}|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s((\x22.\x22)|(\x27.\x27)|(\x5f)?[a-zA-Z](\w|\d)*)|((\x22*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*)\s*(!=|==)\s*((\x22.*\x22)|(\x27.*\x27)|(\x5f)?[a-zA-Z](\w|\d)*))\s*\x29(\x7b(\s|.+)*\x7d)+"

str1 = input("[+] Cadena : ")

print(re.fullmatch(ifRegExp,str1))