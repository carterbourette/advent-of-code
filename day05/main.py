import utility

"""Day 05: Binary Boarding"""

inputs = utility.inputs()


def binary_partition(string, row=range(0, 128), column=range(0, 8)):
    def build_range(_range, is_lower):
        new_range = int(len(_range) / 2)
        if is_lower:
            return range(_range.start, _range.start + new_range)
        return range(_range.stop - new_range, _range.stop)

    if not string:
        return row.start, column.start
    
    command = string[0]

    if command in ('F', 'B'):
        row = build_range(row, command == 'F')
        return binary_partition(string[1:], row, column)
    
    col = build_range(column, command == 'L')
    return binary_partition(string[1:], row, col)


def part1():
    seat_id = lambda x, y: x * 8 + y  
    
    seats = [ seat_id(*binary_partition(ticket)) for ticket in inputs ]

    return utility.solution({ 'max_seat': max(seats) }, test=820)


def part2():
    seat_id = lambda x, y: x * 8 + y  
    
    seats = [ seat_id(*binary_partition(ticket)) for ticket in inputs ]

    seats.sort()

    missing = [ seats[i] + 1 for i in range(len(seats)-1) if seats[i] + 1 != seats[i+1] ]

    return utility.solution({'missing': max(missing)})



if __name__ == '__main__':
    utility.cli()
