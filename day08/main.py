import utility, re
from day08.interpreter import Interpreter

"""Day 08: Handheld Halting"""

inputs = utility.inputs()


def custom(interpreter, executed):
    if interpreter.pc in executed:
        interpreter.suspend = True

    executed.add(interpreter.pc)
    

def part1():
    executed = set()
    bootcode = Interpreter(inputs) \
        .inject(custom, executed) \
        .run()

    return utility.solution({'accumulator': bootcode.accumulator}, test=5)


def part2():    
    idx, found = 0, False
    while not found:        
        temps, executed = [*inputs], set()

        name, _ = temps[idx].split()
        _from, _to = ('jmp','nop') if name == 'jmp' else ('nop','jmp')

        temps[idx] = temps[idx].replace(_from, _to)
        
        bootcode = Interpreter(temps) \
            .inject(custom, executed) \
            .run()

        if not bootcode.suspend:
            found = True

        idx += 1

    return utility.solution({'accumulator': bootcode.accumulator})



if __name__ == '__main__':
    utility.cli()
