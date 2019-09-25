class InstructionLine:
    def __init__(self, instruction, n):
        self.instruction = instruction
        self.Nline = n
        
    def getNline(self):
        return self.Nline  
    
    def getInstruction(self):
        return self.instruction