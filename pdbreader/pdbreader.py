from collections import defaultdict

import pandas as pd

from .specification import SPECIFICATION


def parse_line(line):
    """
    slice a string in specific spots (must include edges,
    left inclusive and right exclusive) and return appropriate types
    """
    line = line.strip()

    for record, spec in SPECIFICATION.items():
        if line.startswith(record):
            items = []
            for rng, dtype, _ in spec:
                field = line[rng[0]:rng[1]]
                try:
                    field = dtype(field.strip())
                except ValueError:
                    field = pd.nan
                items.append(field)
            return record, items
    return None, None


def parse_pdb(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    data = defaultdict(list)
    for line in lines:
        record, fields = parse_line(line)
        if record is not None:
            data[record].append(fields)

    dfs = defaultdict(list)
    for record, fields in data.items():
        _, _, columns = zip(*SPECIFICATION[record])
        df = pd.DataFrame(fields, columns=columns)
        df['record'] = record
        dfs[record] = df
    return dict(dfs)
