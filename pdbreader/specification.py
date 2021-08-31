SPECIFICATION = {
    'ATOM': [
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
        ((60, 66), float, 'b-factor'),
        ((72, 76), str, 'segment'),
        ((76, 78), str, 'element'),
        ((78, 80), str, 'charge'),
    ],
}

SPECIFICATION['HETATM'] = SPECIFICATION['ATOM']
