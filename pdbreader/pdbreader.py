from collections import defaultdict

import pandas as pd

from .specification import SPECIFICATION


def slice_str(str, ranges):
    """
    slice a string in specific spots (must include edges,
    left inclusive and right exclusive)
    """
    items = []
    for rng in ranges:
        field = str[rng[0]:rng[1]]
        items.append(field.strip())
    return items


def slice_line(line):
    line = line.strip()
    for record, spec in SPECIFICATION.items():
        if line.startswith(record):
            fields = slice_str(line, spec['slices'])
            fields_typed = []
            for field, dtype in zip(fields, spec['dtypes']):
                try:
                    field = dtype(field)
                except ValueError:
                    field = pd.nan
                fields_typed.append(field)
            return record, fields
    return None, []


def parse_pdb(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    data = defaultdict(list)
    for line in lines:
        record, fields = slice_line(line)
        if record is not None:
            data[record].append(fields)

    dfs = defaultdict(list)
    for record, fields in data.items():
        columns = SPECIFICATION[record]['columns']
        df = pd.DataFrame(fields, columns=columns)
        df['record'] = record
        dfs[record] = df
    return dict(dfs)
