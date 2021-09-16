# PDB reader
`pdbreader` is a simple python library for parsing PDB (Protein Data Bank) files. It uses pandas DataFrames as its main data structure.

## Installation

```
pip install pdbreader
```

## Usage

```python
import pdbreader

pdb = pdbreader.read_pdb(pdb_path)
```

The resulting `pdb` dictionary contains an entry for each record type (`ATOM`, `CONECT`, etc) in the form of pandas DataFrames.
