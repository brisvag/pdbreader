ATOM = [
    ((6, 11), int, 'id'),
    ((12, 16), str, 'name'),
    ((16, 17), str, 'loc_indicator'),
    ((17, 20), str, 'resname'),
    ((21, 22), str, 'chain'),
    ((22, 26), int, 'resid'),
    ((26, 27), str, 'res_insertion_code'),
    ((30, 38), float, 'x'),
    ((38, 46), float, 'y'),
    ((46, 54), float, 'z'),
    ((54, 60), float, 'occupancy'),
    ((60, 66), float, 'b_factor'),
    ((72, 76), str, 'segment'),
    ((76, 78), str, 'element'),
    ((78, 80), str, 'charge'),
]

CONECT = [
    ((6, 11), int, 'parent'),
    ((11, 16), int, 'bond1'),
    ((16, 21), int, 'bond2'),
    ((21, 26), int, 'bond3'),
    ((26, 31), int, 'bond4'),
    ((31, 36), int, 'h_bond1'),
    ((36, 41), int, 'h_bond2'),
    ((41, 46), int, 'salt_bridge1'),
    ((46, 51), int, 'h_bond3'),
    ((51, 56), int, 'h_bond4'),
    ((56, 61), int, 'salt_bridge2'),
]

SPECIFICATION = {
    'ATOM': ATOM,
    'HETATM': ATOM,
    'CONECT': CONECT,
    # all the following should end the molecule or model
    'TER': [],
    'END': [],
    'ENDMDL': [],
}
