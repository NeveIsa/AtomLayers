import numpy as np


def load_layer_basis(vaspfile):
    b1 = np.loadtxt(vaspfile, skiprows=2, max_rows=1)[:2]
    b2 = np.loadtxt(vaspfile, skiprows=3, max_rows=1)[:2]
    B = np.array([b1, b2]).T
    return B
