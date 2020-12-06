import utility

"""Day 06: Custom Customs"""

inputs = utility.inputs(lambda x: x.split(), pre_process='\n\n')

distinct_answer = lambda group: set.union(*group)
distinct_group  = lambda group: set.intersection(*group)

groups = [ [ set(ans) for ans in group ] for group in inputs ]


def part1():
    answers = map(len, map(distinct_answer, groups))
    
    return utility.solution({ 'sum': sum(answers) }, test=11)


def part2():
    answers = map(len, map(distinct_group, groups))

    return utility.solution({ 'sum': sum(answers) }, test=6)



if __name__ == '__main__':
    utility.cli()
