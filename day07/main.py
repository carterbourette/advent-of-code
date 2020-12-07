import utility, re

"""Day 07: Handy Haversacks"""

inputs = utility.inputs(lambda x: re.sub(r' bags?|\.','',x))
DELIMETER = ' contain |, '
TARGET    = 'shiny gold'

def traverse(t, key, previous=set()): 
    current = t.get(key, [])

    for node in current:
        previous.add(node)

    [ traverse(t, node) for node in current ]
    
    return len(previous)


def count_bags(t, name, qty=1):
    count, current = 0, t[name]

    for bag in current:
        if bag == 'no other': continue

        num_bags, next_bag = int(bag[0]), bag[2:]
        count += num_bags * (1 + count_bags(t, next_bag, num_bags))
    
    return count


def part1():
    tree = {}
    for line in inputs:
        root, *children = re.split(DELIMETER, line)

        for child in children:
            if child == 'no other': continue
            key = child[2:]
            tree[key] = [ *tree.get(key, []), root ]

    return utility.solution({ 'bags': traverse(tree, TARGET) }, test=4)


def part2():
    bags = {}
    for line in inputs:
        root, *children = re.split(DELIMETER, line)
        bags[root] = children

    return utility.solution({ 'count': count_bags(bags, TARGET) })



if __name__ == '__main__':
    utility.cli()
