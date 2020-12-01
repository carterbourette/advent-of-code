from collections import namedtuple
import sys, inspect

args = sys.argv

def inputs(parse=lambda x : x):
    day = args[0].split('/')[-2]

    with open(f'{day}/input.txt') as fp:
        return [ parse(line.strip()) for line in fp ]


def log(*args):
    print(*args)


def solution(d={}):
    return namedtuple('Solution', d.keys())(**d) 


def cli():
    """CLI Parser
    call a function via the command line.
    Usage: `python3 -m day00.main part1` or `python3 -m day00.main part1`
    """
    if len(args) < 2: 
        return
    
    call_list = ['part1', 'part2'] if args[1] == 'all' else [ args[1] ]

    for name in call_list:
        function = inspect.stack()[1][0].f_globals.get(name, None)
        
        if not function: 
            log(name, 'not found in module.')
            return
        
        retval = function()
        if retval:
            log(f'{name}:', retval)
