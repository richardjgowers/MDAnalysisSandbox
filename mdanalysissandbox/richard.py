"""Hey this is my cool module


"""

import numpy as np

def count_names(ag, name):
    """Count how many atoms have a particular name

    Parameters
    ----------
    ag : AtomGroup
      the atomgroup to work on
    name : str
      the name to look for

    Returns
    -------
    count : int
      the number of atoms with this name
    """
    return len(ag[ag.names == name])
