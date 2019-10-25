class InstructionLine:
    def __init__(self, instruction, n, type):
        self.instruction = instruction
        self.Nline = n
        self.type = type
        
    def getNline(self):
        return self.Nline  
    
    def getInstruction(self):
        return self.instruction

    def getType(self):
        return self.type