import utility

"""Day 03: Toboggan Trajectory """

grid = utility.inputs()


def check_slope(grid, x, y):
    trees, pos = 0, 0
    for idx, row in enumerate(grid):
        if idx % y != 0:
            continue
        
        if row[pos % len(row)] == '#':
            trees += 1

        pos += x

    return trees


def part1():
    trees = check_slope(grid, 3, 1)

    return utility.solution({ 'trees': trees })


def part2():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    product = 1
    for x, y in slopes:
        product *= check_slope(grid, x, y)

    return utility.solution({ 'product': product })



if __name__ == '__main__':
    utility.cli()
