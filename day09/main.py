import utility

"""Day 09: Encoding Error"""

inputs = utility.inputs(lambda x: int(x))

BUFFER, SUM_TO = 25, 138879426
if utility.TEST_FLAG:
    BUFFER, SUM_TO = 5, 127


def part1():
    idx = BUFFER
    while idx < len(inputs):
        preamble = inputs[idx-BUFFER:idx]
        cmp = inputs[idx]
        
        found = False
        for x in preamble:
            if (cmp - x) in preamble:
                found = True
        
        if not found:
            return utility.solution({'val': cmp}, test=127)
        idx += 1


def part2():
    start = 0
    while True:
        idx, total, walk = start, 0, []
        while total < SUM_TO:
            total += inputs[idx]
            walk.append(inputs[idx])
            
            if total == SUM_TO:
                return utility.solution({'val': min(walk) + max(walk) }, test=None)
            
            idx += 1
        start += 1



if __name__ == '__main__':
    utility.cli()
