# /usr/bin/python3

from collections import deque, OrderedDict
from copy import deepcopy
from grid import Grid


def main():
    starting_grid = Grid(2, 3)
    moves = []
    found_combos = find_combos(starting_grid, moves)
    for puzzle,moves in found_combos.items():
        print(moves)
        puzzle.pprint()
        print()

    print(f'Puzzle: {starting_grid.rows}x{starting_grid.columns}')
    print(f'Found Combos: {len(found_combos)}')

#    test_puzzle = Grid(3, 3)
#    test_puzzle.values = [1, 2, 3, 4, 5, 6, 8, 7, None]
#    print('Test Puzzle in found combos? {}'
#          ''.format(any(puzzle[0]==test_puzzle for puzzle in found_combos)))
    test_puzzle = Grid(2, 3)
    test_puzzle.values = [1, 2, 3, 5, 4, None]
    print('Test Puzzle in found combos? {}'
          ''.format(any(puzzle[0]==test_puzzle for puzzle in found_combos)))


def find_combos(puzzle_grid, moves):
    """ Take the current state of the puzzle and try each of the combos to find
    new states of the game board.
    """
    combos = OrderedDict()
    start_combo = (puzzle_grid, moves)
    combos[puzzle_grid] = moves
    new_combos = deque()
    new_combos.append(start_combo)

    while new_combos:
        puzzle_grid, moves = new_combos.popleft()

        for direction in ['Up', 'Down', 'Left', 'Right']:
            # TODO: We could use the previous one if the previous move was invalid.
            new_puzzle = deepcopy(puzzle_grid)
            try:
                new_puzzle.move(direction)
            except RuntimeError:
                pass # Not a valid move
            else:
                if new_puzzle not in combos:
                    # Record the move and recursively check for new moves
                    new_moves = deepcopy(moves)
                    new_moves.append(direction)
                    combos[new_puzzle] = new_moves
                    new_combos.append((new_puzzle, new_moves))

    return combos

if __name__ == '__main__':
    import timeit
    t = timeit.Timer('main()')
    print(f'Executing 3 times: {t.timeit(3)} seconds')
    # Executing 3 times: 8.805438807001337 seconds
