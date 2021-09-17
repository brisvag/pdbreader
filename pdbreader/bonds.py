import numpy as np
from scipy.spatial.ckdtree import cKDTree

from .atom_data import VDW


def guess_bonds(atoms, fudge=1.2):
    """
    guess bonds based on distances and vdw radii
    """
    if len(atoms) == 0:
        return np.empty((0, 2))

    coords = atoms[['x', 'y', 'z']].to_numpy()
    elem = atoms['element'].to_numpy()

    max_dist = np.max([VDW.get(el, 0) for el in np.unique(elem)] or 0)

    if max_dist == 0:
        return np.empty((0, 2))

    # get all neighbours
    tree = cKDTree(coords)
    matrix = tree.sparse_distance_matrix(tree, max_dist * fudge)
    pairs, dists = zip(*matrix.items())

    # discard duplicates (symmetric matrix)
    pairs = np.array(pairs)
    non_duplicate = pairs[:, 0] < pairs[:, 1]
    pairs = pairs[non_duplicate]

    # get vdw radii for each pair and calculate their distance
    elem_pairs = elem[pairs]
    vdw_pairs = np.vectorize(lambda x: VDW.get(x, -1))(elem_pairs)
    vdw_dists = vdw_pairs.sum(axis=1) * fudge

    # bonds are where the actual distance is less than the sum of the vdw radii
    dists = np.array(dists)[non_duplicate]
    bonds = dists <= vdw_dists

    # find inter-residue H-bonds
    hydro = np.any(elem_pairs == 'H', axis=1)
    resid = atoms['resid'].to_numpy()
    same_resid = np.equal.reduce(resid[pairs], axis=1)
    hydro_same_resid = np.logical_and(hydro, same_resid)

    # find where both are hydrogens
    both_hydro = np.all(elem_pairs == 'H', axis=1)

    # discard if inter-residue H-bonds or both hydrogens
    keep = np.logical_and(~both_hydro, ~hydro_same_resid)

    return pairs[np.logical_and(bonds, keep)]
