from utils import *


# `grid` is defined in the test code scope as the following:
# (note: changing the value here will _not_ change the test code)
grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    dict={}
    new_dict = {}
    values_set = set({"1","2","3","4","5","6","7","8","9"})
    cols = "123456789"
    rows = "ABCDEFGHI"
    keys = cross(rows, cols)

    values = list(grid)

    for i in range(len(values)) :
        dict[keys[i]] = values[i]
    for key in cross(rows, cols):
        if dict[key] == ".":
            forbidden_set = set()
            cols_search, rows_search, block  = units[key]
            for key1 in cols_search:
                if(dict[key1] != "."):
                    forbidden_set.add(dict[key1])
            for key1 in rows_search:
                if(dict[key1] != "."):
                    forbidden_set.add(dict[key1])
            for key1 in block:
                if(dict[key1] != "."):
                    forbidden_set.add(dict[key1])

            diff = values_set - forbidden_set
            forbidden = "".join(diff)
            new_dict[key] = forbidden
            # for a, b in zip(forbid, cols):
            #     if a != b:
            #         print(str(a) + str(b))
            #new_dict[key] = forbid
        else:
            new_dict[key] = dict[key]


    display(new_dict)
    #display(dict)


grid_values(grid)