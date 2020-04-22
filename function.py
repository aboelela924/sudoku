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
    dict = {}
    new_dict = {}
    values_set = set({"1", "2", "3", "4", "5", "6", "7", "8", "9"})
    cols = "123456789"
    rows = "ABCDEFGHI"
    keys = cross(rows, cols)

    values = list(grid)

    for i in range(len(values)):
        dict[keys[i]] = values[i]
    for key in cross(rows, cols):
        if dict[key] == ".":
            forbidden_set = set()
            cols_search, rows_search, block = units[key]
            for key1 in cols_search:
                if (dict[key1] != "."):
                    forbidden_set.add(dict[key1])
            for key1 in rows_search:
                if (dict[key1] != "."):
                    forbidden_set.add(dict[key1])
            for key1 in block:
                if (dict[key1] != "."):
                    forbidden_set.add(dict[key1])

            diff = values_set - forbidden_set
            forbidden = "".join(diff)
            new_dict[key] = forbidden
        else:
            new_dict[key] = dict[key]
    return new_dict


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    first_element_unit = ["A1", "A4", "A7", "D1", "D4", "D7", "G1", "G4", "G7"]
    for key in first_element_unit:
        unit = units[key][2]
        all_numbers = []
        for box_key in unit:
            if (len(values[box_key]) > 1):
                nums = list(values[box_key])
                all_numbers.extend(nums)
        number_appearance_dict = {}
        for num in all_numbers:
            number_appearance_dict[num] = number_appearance_dict.get(num, 0) + 1
        singles = get_only_appearence(number_appearance_dict)
        if len(singles) > 0:
            for single in singles:
                for box_key in unit:
                    if (len(values[box_key]) > 1 and single in values[box_key]):
                        values[box_key] = single


    return values


new_grid = grid_values(grid)
new_grid = only_choice(new_grid)
display(new_grid)