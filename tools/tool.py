import numpy as np


def load_layer_bases(firstlayer_vaspfile, secondlayer_vaspfile):
    # Load A and G from vasp file
    ### first layer
    a1 = np.loadtxt(firstlayer_vaspfile, skiprows=2, max_rows=1)[:2]
    a2 = np.loadtxt(firstlayer_vaspfile, skiprows=3, max_rows=1)[:2]
    A = np.array([a1, a2]).T
    ### second layer
    g1 = np.loadtxt(secondlayer_vaspfile, skiprows=2, max_rows=1)[:2]
    g2 = np.loadtxt(secondlayer_vaspfile, skiprows=3, max_rows=1)[:2]
    G = np.array([g1, g2]).T

    return A, G
