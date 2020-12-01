import utility

"""Day 1: Report Repair"""

inputs = utility.inputs(parse=lambda x: int(x))

def part1():
    """Find two entries in the input file that add to 2020, report the product."""
    for e1 in inputs:
        for e2 in inputs:
            if e1 + e2 == 2020:
                return utility.solution({ 'product': e1 * e2, 'numbers': (e1, e2) })


def part2():
    """Find three entries in the input file that add to 2020, report the product."""
    for e1 in inputs:
        for e2 in inputs:
            for e3 in inputs:
                if e1 + e2 + e3 == 2020:
                    return utility.solution({ 'product': e1 * e2 * e3, 'numbers': (e1, e2, e3) })



if __name__ == '__main__':
    utility.cli()
