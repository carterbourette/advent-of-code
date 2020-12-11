import utility
from functools import lru_cache

"""Day 10: Adapter Array"""

inputs = utility.inputs(lambda x: int(x))


def part1():
    jolts = sorted([*inputs])

    one_jolt, three_jolt, prev = 0, 0, 0
    for jolt in jolts:
        diff = jolt - prev

        if diff == 1:
            one_jolt += 1
        elif diff == 3:
            three_jolt += 1

        prev = jolt

    return utility.solution({'sol': one_jolt * (three_jolt + 1)}, test=220)


def part2():
    jolts = sorted([0, *inputs, max(inputs) + 3])
    MAX = len(jolts)

    def cmp(i, j):
        return jolts[j] - jolts[i] <= 3

    @lru_cache
    def arrange(i):
        if i == MAX - 1:
            return 1

        return sum([arrange(j) for j in range(i+1, min(i+4, MAX)) if cmp(i,j)])

    return utility.solution({'sol': arrange(0)}, test=None)


if __name__ == '__main__':
    utility.cli()
