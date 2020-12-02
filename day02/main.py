import utility

"""Day 2: Password Philosophy"""

inputs = utility.inputs(lambda x: x.split(' '))

def part1():
    valid = 0
    for bound, letter, password in inputs:
        count = password.count(letter[0])

        lower, upper = [ int(b) for b in bound.split('-')]

        if count >= lower and count <= upper:
            valid += 1

    return utility.solution({ 'valid': valid })


def part2():
    valid = 0
    for bound, letter, password in inputs:
        lower, upper = [ int(b) for b in bound.split('-')]
        
        lp, up = password[lower - 1], password[upper - 1]
    
        if (lp == letter[0]) ^ (up == letter[0]):
            valid += 1

    return utility.solution({ 'valid': valid })



if __name__ == '__main__':
    utility.cli()
