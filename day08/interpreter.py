import re, operator

class Interpreter:
    """Our Boot Code Interpreter"""

    def __init__(self, instructions):
        self.instructions = [ Instruction(_) for _ in instructions ]
        self.suspend = False
        self.pc = 0
        self._acc = 0

        self.injections = []

    
    @property
    def accumulator(self):
        return self._acc


    def jmp(self, instruction): 
        self.pc = instruction.op(self.pc, instruction.val)
        return True


    def acc(self, instruction):
        self._acc = instruction.op(self._acc, instruction.val)


    def inject(self, func, *args):
        self.injections.append((func, args))
        
        return self


    def run(self):
        while True:
            [ inject(self, *args)  for inject, args in self.injections ]

            if self.pc >= len(self.instructions) or self.suspend: 
                break

            instruction = self.instructions[self.pc]
            
            func = getattr(self, instruction.name, lambda _: None)
        
            interrupt = func(instruction)
            if not interrupt:
                self.pc += 1
        
        return self



class Instruction:

    def __init__(self, raw):
        name, op, val = re.findall(r'(\w+) ([+-])(\d+)', raw)[0]

        self.raw = raw
        self.name = name
        self.op = Instruction.string_to_operator(op)
        self.val = int(val)
    

    def __str__(self):
        return self.raw

    
    @staticmethod
    def string_to_operator(op):
        return {
            '+': operator.add,
            '-': operator.sub
        }[op]
