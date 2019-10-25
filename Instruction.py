class Instruction():
    def __init__(self, instruction, message, line):
        self.instruction = instruction
        self.message = message
        self.line = line

    def getMessage(self):
        return self.message

    def setLine(self, l):
        self.line = l

    def getLine(self):
        return self.line
    
    def getInstruction(self):
        return self.instruction
    