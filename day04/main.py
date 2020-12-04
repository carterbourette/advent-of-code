import utility

"""Day 04: Passport Processing"""

inputs = utility.inputs(
    parse=lambda line: [ field for field in line.split() ], 
    pre_process='\n\n'
)

def valid_height(x):
    is_cm = x.endswith('cm') and 150 <= int(x[:-2]) <= 193
    is_in = x.endswith('in') and 59 <= int(x[:-2]) <= 76
    return is_cm or is_in

FIELDS = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': valid_height,
    'hcl': lambda x: x[0] == '#' and len(x) == 7 and all(c.isdigit() or c in 'abcdef' for c in x[1:]),
    'ecl': lambda x: x in ('amb','blu','brn','gry','grn','hzl','oth'),
    'pid': lambda x: len(x) == 9 and all(c.isdigit() for c in x)
}
REQUIRED = set(FIELDS)

def parse():
    records = []
    for line in inputs:
        record = {}
        for field in line:
            key, val = field.split(':')
            record[key] = val
        records.append(record)

    return records


def part1():
    records = parse()
    valid = sum(1 for record in records if set(record.keys()) >= REQUIRED)
    
    return utility.solution({ 'valid': valid }, test=2)


def part2():
    records = parse()
    valid = 0
    for record in records:
        is_super = set(record.keys()) >= REQUIRED 

        if is_super and all(validator(record[field]) for field, validator in FIELDS.items()):
            valid += 1

    return utility.solution({ 'valid': valid })



if __name__ == '__main__':
    utility.cli()
