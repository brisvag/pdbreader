from collections import defaultdict

import pandas as pd

from .specification import SPECIFICATION


def parse_line(line):
    """
    slice a string in specific spots (must include edges,
    left inclusive and right exclusive) and return appropriate types
    """
    line = line.strip()

    for record_type, spec in SPECIFICATION.items():
        if line.startswith(record_type):
            items = []
            for rng, dtype, _ in spec:
                field = line[rng[0]:rng[1]]
                try:
                    field = dtype(field.strip())
                except ValueError:
                    field = None
                items.append(field)
            return record_type, items
    return None, None


def parse_pdb(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    data = defaultdict(list)
    for line in lines:
        record_type, fields = parse_line(line)
        if record_type is not None:
            data[record_type].append(fields)

    dfs = defaultdict(list)
    for record_type, fields in data.items():
        _, _, columns = zip(*SPECIFICATION[record_type])
        df = pd.DataFrame(fields, columns=columns)
        dfs[record_type] = df
    return dict(dfs)
