#! /usr/bin/python3

from copy import deepcopy


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.values = list(range(1, rows*columns))
        self.values.append(None)

    def __eq__(self, rhs):
        return ((self.rows == rhs.rows)
            and (self.columns == rhs.columns)
            and (self.values == rhs.values))

    def __deepcopy__(self, memo):
        dc = Grid(self.rows, self.columns)
        dc.values = deepcopy(self.values)
        return dc

    def get_position(self, value):
        idx = self.values.index(value)
        col = idx % self.columns
        row = idx // self.columns
        return (col, row)

    def _get(self, col, row):
        if 0<=row<self.rows and 0<=col<self.columns:
            return self.values[row*self.columns + col]
        raise ValueError(f'col={col} and row={row} outside of range!')

    def _set(self, col, row, value):
        if 0<=row<self.rows and 0<=col<self.columns:
            self.values[row*self.columns + col] = value
        else:
            raise ValueError(f'col={col} and row={row} outside of range!')

    def move(self, direction):
        col,row = self.get_position(None)
        if direction == 'Up':
            if row == (self.rows-1):
                raise RuntimeError('Cannot move Up')
            self._set(col, row, self._get(col, row+1))
            self._set(col, row+1, None)
        elif direction == 'Down':
            if row == 0:
                raise RuntimeError('Cannot move Down')
            self._set(col, row, self._get(col, row-1))
            self._set(col, row-1, None)
        elif direction == 'Left':
            if col == (self.columns-1):
                raise RuntimeError('Cannot move Left')
            self._set(col, row, self._get(col+1, row))
            self._set(col+1, row, None)
        elif direction == 'Right':
            if col == 0:
                raise RuntimeError('Cannot move Right')
            self._set(col, row, self._get(col-1, row))
            self._set(col-1, row, None)
        else:
            raise ValueError(f'Invalid direction: {direction}')

    def pprint(self):
        v_iter = iter(self.values)
        for row in range(self.rows):
            print('+----'*self.columns + '+')
            for column in range(self.columns):
                value = next(v_iter)
                if value:
                    print(f'| {value:2} ', end='')
                else:
                    print('|    ', end='')
            print('|')
        print('+----'*self.columns + '+')
