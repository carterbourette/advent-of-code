from collections import namedtuple
import sys, inspect

args = sys.argv
TEST_FLAG = '--test' in args

def inputs(parse=lambda x : x, pre_process='\n'):
    day = args[0].split('/')[-2]

    file = f'{day}/input.txt' if not TEST_FLAG else f'{day}/test.txt'

    with open(file) as fp:
        contents = fp.read().split(pre_process)
        return [ parse(line) for line in contents ]


def log(*args):
    print(*args)


def solution(d={}, test=None):
    return namedtuple('Solution', d.keys())(**d), test


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
        
        retval, test = function()
        if retval:
            log(f'{name}:', retval)

            if TEST_FLAG and test != None:
                assert retval[0] == test, f'Expected `{test}`, got `{retval[0]}`'
