class Instruction():
    def __init__(self, instruction, message):
        self.instruction = instruction
        self.message = message
    
    def getMessage(self):
        return self.message
    
    def getInstruction(self):
        return self.instruction
    